# coding:utf-8

from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from tslearn.clustering import TimeSeriesKMeans
import numpy as np


class TsCluster:
    def __init__(self, df, center_num=4):
        self.input_df = df
        self.data_scaled = None
        self.center_num = center_num
        self.labels = None
        self.fitted_cluster = None

    def reshape_data(self):
        ts_value = self.input_df.T.values
        ts_value = ts_value.reshape(ts_value.shape[0], ts_value.shape[1], 1)
        scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.)
        data_scaled = scaler.fit_transform(ts_value)
        data_scaled = np.nan_to_num(data_scaled)
        self.data_scaled = data_scaled

    def get_one_label_index(self, one_class):
        one_label_index = []
        labels = self.labels
        for i in range(len(labels)):
            if labels[i] == one_class:
                one_label_index.append(i)
        return one_label_index

    def fit_tskmeans(self):
        data_scaled = self.data_scaled
        center = self.center_num
        km = TimeSeriesKMeans(n_clusters=center, metric="softdtw", max_iter=5, verbose=False, random_state=0).fit(
            data_scaled)
        self.fietted_cluster = km
        self.labels = km.labels_

    def run(self):
        self.reshape_data()
        self.fit_tskmeans()
        
