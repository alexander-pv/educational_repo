import dataclasses
import os


class Dataset:
    def __init__(self, root: str, files: dict or str):
        """
        Datasets wrapper
        :param root: str, data root path
        :param files: dict of filenames/directory names
        """
        self.root = root
        self.files = files
        self._build_paths()

    def _build_paths(self) -> None:
        if isinstance(self.files, dict):
            for k, v in self.files.items():
                setattr(self, k, os.path.join(self.root, v))
        else:
            setattr(self, self.files, os.path.join(self.root, self.files))


@dataclasses.dataclass
class DatasetsInfo:
    copd_data: Dataset


data_info = DatasetsInfo(
    copd_data=Dataset(root=os.path.join('..', 'data', 'COPD_Patients_Dataset'),
                      files={'data': 'copd_dataset.csv'}
                      ),
)
