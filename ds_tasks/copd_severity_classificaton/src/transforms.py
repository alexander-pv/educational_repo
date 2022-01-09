import pandas as pd
from sklearn.base import TransformerMixin


class RemoveColumns(TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.feature_names = None

    def transform(self, x):
        data = x.copy()
        data = data[[x for x in data.columns if x not in self.columns]]
        self.feature_names = data.columns.tolist()
        return data

    def fit(self, data, y=None):
        return self


class RemoveRows(TransformerMixin):
    def __init__(self, row_ids):
        self.row_ids = row_ids
        self.feature_names = None

    def transform(self, x):
        data = x.copy()
        data = data.loc[~data.index.isin(self.row_ids)]
        data = data.reset_index(drop=True)
        self.feature_names = data.columns.tolist()
        return data

    def fit(self, data, y=None):
        return self


class AddFeatures(TransformerMixin):
    def __init__(self, features_agg):
        self.features_agg = features_agg
        self.feature_names = None

    def transform(self, x):
        data = x.copy()
        for feature_name, func in self.features_agg.items():
            data[feature_name] = func(data)
        self.feature_names = data.columns.tolist()
        return data

    def fit(self, data, y=None):
        return self


class RecodeFeatures(TransformerMixin):
    def __init__(self, recode_dict):
        self.recode_dict = recode_dict
        self.feature_names = None

    def transform(self, x):
        data = x.copy()
        for feature_name, codes_map in self.recode_dict.items():
            data[feature_name] = data[feature_name].map(codes_map)
        self.feature_names = data.columns.tolist()
        return data

    def fit(self, data, y=None):
        return self


class PandasOneHotEncode(TransformerMixin):
    """
    OneHotEncoder workaround for DataFrames without ColumnTransformers
    """

    def __init__(self, columns):
        self.columns = columns
        self.feature_names = None

    def transform(self, x):
        data = x.copy()
        for c in self.columns:
            data = pd.concat([data, pd.get_dummies(data[c], prefix=c)], axis=1)
            data = data.drop(columns=c)
        self.feature_names = data.columns.tolist()
        return data

    def fit(self, data, y=None):
        return self
