import torch.nn as nn


class RDClassifier(nn.Module):

    def __init__(self, input_shape: tuple, n_classes: int, kernels: tuple = (5, 5, 2, 5),
                 strides: tuple = (1, 1, 2, 1), dropout: float = 0.2):
        super(RDClassifier, self).__init__()

        n_feats = input_shape[2]
        for kernel, stride in zip(kernels, strides):
            n_feats = get_output(n_feats, kernel, 0, stride)
        self.conv1 = nn.Conv1d(in_channels=input_shape[1], out_channels=128, kernel_size=kernels[0])
        self.conv2 = nn.Conv1d(in_channels=128, out_channels=256, kernel_size=kernels[1])
        self.maxpool = nn.MaxPool1d(kernel_size=kernels[2])
        self.conv3 = nn.Conv1d(in_channels=256, out_channels=512, kernel_size=kernels[3])
        self.dropout = nn.Dropout(dropout)
        self.linear1 = nn.Linear(int(512 * n_feats), 1024)
        self.linear2 = nn.Linear(1024, n_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.maxpool(x)
        x = self.relu(self.conv3(x))
        x = self.dropout(x)
        x = x.flatten(start_dim=1)
        x = self.relu(self.linear1(x))
        x = self.linear2(x)
        return x


def get_output(size: int, kernel: int, pad: int, stride: int) -> int:
    return int((size - kernel + 2 * pad) / stride + 1)
