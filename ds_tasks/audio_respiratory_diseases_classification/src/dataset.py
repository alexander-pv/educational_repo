import glob
import os

import pandas as pd
import torch
import torchaudio
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset


class RespiratoryDataset(Dataset):

    def __init__(self, annotation_path: str, audio_dir: str, transform: callable or tuple,
                 target_sample_rate: int, name: str, seed: int, train_size: float or None = None,
                 val_size: float or None = None, exclude_classes: tuple = ()):
        """
        RespiratoryDataset class based on UrbanSoundDataset
        :param annotation_path:    str, path to the wav labels
        :param audio_dir:          str, path to the wav directory
        :param transform:          str,
        :param target_sample_rate: int,
        :param dataset name:       str,
        :param train_size:         float, optional
        :param val_size:           float, optional
        :param exclude_classes:    tuple of str, optional
        """
        self.audio_dir = audio_dir
        self.annotation_path = annotation_path
        self.exclude_classes = exclude_classes
        self.transform = transform
        self.target_sample_rate = target_sample_rate
        self.train_size = train_size
        self.val_size = val_size
        self.name = name
        self.seed = seed

        self.annotations = self.load_annotations()
        self.df_prepared_annot = self.prepare_annotation_table()
        self.subset_annotation = self.df_prepared_annot
        self.class_map = self.make_class_map()
        if train_size and val_size:
            assert self.name in ('train', 'test', 'val')
            train_idx, val_idx, test_idx = self.split_dataset()
            self.data_idx = {'train': train_idx, 'val': val_idx, 'test': test_idx}
            self.subset_annotation = self.subset_annotation[self.subset_annotation.index.isin(self.data_idx[self.name])]
            self.subset_annotation = self.subset_annotation.reset_index(drop=True)
        print(f'{self.name} subset was created. Size: {self.__len__()}')

    def __len__(self):
        return self.subset_annotation.shape[0]

    def __getitem__(self, index: int):
        label = self.get_label(index)
        signal, sr = self.load_wav(index)
        signal = self.resample(signal, sr)
        if callable(self.transform):
            signal = self.transform(signal)
        elif isinstance(self.transform, tuple):
            signal = self.make_transforms(signal)
        return signal, label

    def load_annotations(self):
        return pd.read_csv(self.annotation_path, dtype={'patient_id': int, 'class_label': str})

    def prepare_annotation_table(self) -> pd.DataFrame:
        prepared_annot = []
        for filepath in glob.glob(os.path.join(self.audio_dir, "*.wav")):
            filename = filepath.split(os.sep)[-1]
            patient_id = int(filename.split('_')[0])
            class_label = self.annotations[self.annotations['patient_id'] == patient_id]['class_label'].iloc[0]
            if class_label not in self.exclude_classes:
                prepared_annot.append((patient_id, class_label, filepath))
        df_prepared_annot = pd.DataFrame(prepared_annot, columns=('patient_id', 'class_label', 'wav_path'))
        return df_prepared_annot

    def load_wav(self, index: int) -> torch.Tensor and int:
        path = self.subset_annotation.iloc[index]['wav_path']
        signal, sr = torchaudio.load(path)
        return signal, sr

    def get_label(self, index: int) -> int:
        label = self.subset_annotation.iloc[index]['class_label']
        return self.class_map[label]

    def make_class_map(self) -> dict:
        sorted_class_names = sorted(self.df_prepared_annot['class_label'].unique().tolist())
        cls_map = dict([(j, i) for i, j in enumerate(sorted_class_names)])
        print(f'{self.name} subset classes mapping:\n{cls_map}')
        return cls_map

    def split_dataset(self):
        idxs, labels = self.subset_annotation.index, self.subset_annotation['class_label']
        train_idxs, test_idxs, train_labels, test_labels = train_test_split(idxs,
                                                                            labels,
                                                                            stratify=labels,
                                                                            test_size=1 - self.train_size,
                                                                            random_state=self.seed)
        val_idxs, test_idxs, val_labels, test_labels = train_test_split(test_idxs,
                                                                        test_labels,
                                                                        stratify=test_labels,
                                                                        test_size=1 - self.val_size,
                                                                        random_state=self.seed)

        return train_idxs, val_idxs, test_idxs

    def resample(self, signal: torch.Tensor, sr: int) -> torch.Tensor:
        if sr != self.target_sample_rate:
            resampler = torchaudio.transforms.Resample(sr, self.target_sample_rate)
            signal = resampler(signal)
        return signal

    def make_transforms(self, signal: torch.Tensor) -> torch.Tensor:
        output = []
        for t in self.transform:
            output.append(torch.mean(t(signal), 2))
        return torch.cat(output, dim=1)

    @staticmethod
    def mix_down(signal: torch.Tensor) -> torch.Tensor:
        if signal.shape[0] > 1:
            signal = torch.mean(signal, dim=0, keepdim=True)
        return signal
