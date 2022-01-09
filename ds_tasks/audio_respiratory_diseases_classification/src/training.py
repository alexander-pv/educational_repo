import datetime
import os

import numpy as np
import torch
import tqdm
from sklearn.metrics import classification_report


class SaveBestModelCallback:

    def __init__(self, model_name: str, class_dict: dict, save_path: str, val_loss: float or None = None):

        self.current_best_val_loss = val_loss if val_loss else np.inf
        self.model_name = model_name
        self.class_dict = class_dict
        self.save_path = save_path

    def check_loss_improvement(self, net: torch.nn.Module, epoch: int, val_loss: float):

        if self.current_best_val_loss:
            if val_loss < self.current_best_val_loss:
                full_save_path = os.path.join(self.save_path, f'pytorch_{self.model_name}_epoch_{epoch}.pth')
                torch.save(net.state_dict(), full_save_path)
                print(f'[{self.__class__.__name__}] ' +
                      f'val_loss was improved: {self.current_best_val_loss} -> {val_loss}. Model was saved.')
                self.current_best_val_loss = val_loss

    def validate(self, net, criterion, epoch, val_loader, target_names, device):

        y_true, y_pred = [], []

        with torch.no_grad():
            val_loss = 0.0

            for i, val_batch in enumerate(tqdm.tqdm(val_loader)):
                inputs, labels = val_batch[0], val_batch[1]
                y_true.extend(labels.cpu().numpy().tolist())
                inputs, labels = inputs.to(device), labels.to(device)

                outputs = net(inputs)
                val_loss += criterion(outputs, labels)
                _, indicies = torch.max(outputs, 1)
                y_pred.extend(indicies.cpu().numpy().tolist())

            val_loss /= val_loader.__len__()
            self.check_loss_improvement(net, epoch, val_loss)

        report_out_dict, report_out_txt = get_classification_report(y_true, y_pred, target_names)
        torch.cuda.empty_cache()
        return val_loss, report_out_dict, report_out_txt


def model_train(net, train_loader, val_loader, epochs, optimizer, criterion, scheduler, device,
                save_path, class_dict, model_name, verbose=0, display_step=20, epoch_start=1):
    save_best_callback = SaveBestModelCallback(model_name=model_name,
                                               class_dict=class_dict,
                                               save_path=save_path)

    net.to(device)

    for epoch in range(epoch_start, epochs):
        torch.cuda.empty_cache()
        net.train()
        running_loss = 0.0
        t0 = datetime.datetime.now()

        for i, train_batch in enumerate(tqdm.tqdm(train_loader), start=1):

            inputs, labels = train_batch[0], train_batch[1]
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() / train_batch[0].shape[0]

            if verbose:
                if i % display_step == 0:
                    print(f'[Training] [Epoch: {epoch}. Batch: {i}] ' +
                          '[sum_loss: %.3f]' % running_loss
                          )

        net.eval()
        val_loss, cls_report_dict, cls_report = \
            save_best_callback.validate(
                net, criterion, epoch, val_loader, list(val_loader.dataset.class_map.keys()), device)

        scheduler.step(val_loss)
        current_lr = optimizer.param_groups[0]['lr']
        t1 = datetime.datetime.now()

        print(f'[{(t1 - t0).total_seconds()} sec.][Epoch {epoch}] ' +
              f'train_loss: {running_loss}, val_loss: {val_loss}, learning_rate: {current_lr}.')
        if verbose:
            print(cls_report)


def get_classification_report(y_true: list, y_pred: list, target_names: list) -> dict and str:
    out_dict = classification_report(y_true, y_pred, target_names=target_names, output_dict=True)
    out_txt = classification_report(y_true, y_pred, target_names=target_names, output_dict=False)
    return out_dict, out_txt


def set_weighted_loss(label_to_count: dict, device: str) -> torch.FloatTensor:
    weights = {k: 1 / v for k, v in label_to_count.items()}
    normed_weights = {k: v / sum(weights.values()) for k, v in weights.items()}

    loss_weight = [v for k, v in sorted(normed_weights.items(), key=lambda x: x[0])]
    loss_weight = torch.FloatTensor(loss_weight).to(device)
    return loss_weight


def evaluate(net, test_loader, device):
    y_true, y_pred = [], []
    target_names = list(test_loader.dataset.class_map.keys())
    with torch.no_grad():
        for i, val_batch in enumerate(tqdm.tqdm(test_loader)):
            inputs, labels = val_batch[0], val_batch[1]
            y_true.extend(labels.cpu().numpy().tolist())
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = net(inputs)
            _, indicies = torch.max(outputs, 1)
            y_pred.extend(indicies.cpu().numpy().tolist())

    report_out_dict, report_out_txt = get_classification_report(y_true, y_pred, target_names)
    torch.cuda.empty_cache()
    return report_out_dict, report_out_txt
