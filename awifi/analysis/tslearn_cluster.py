from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from tslearn.clustering import KShape
from tslearn.clustering import GlobalAlignmentKernelKMeans
from tslearn.clustering import TimeSeriesKMeans
import numpy as np

def get_normal_tslearn_data(df):
    ts_value = df.T.values
    ts_value = ts_value.reshape(ts_value.shape[0],ts_value.shape[1],1)
    scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.)
    data_scaled = scaler.fit_transform(ts_value)
    data_scaled = np.nan_to_num(data_scaled)
    return data_scaled

def get_one_lable_index(lables,class1):
    lab_1 = []
    for i in range(len(labels)):
        if(labels[i] == class1):
            lab_1.append(i)
    return lab_1

def kshape(data_scaled,center=10):
    ks = KShape(n_clusters=center, n_init=1, verbose=False, random_state=0).fit(data_scaled)
    return ks

def GAK_km(data_scaled,center=10):
    gak_km = GlobalAlignmentKernelKMeans(n_clusters=center, verbose=False, random_state=0).fit(data_scaled)
    return gak_km

def TSKMeans(data_scaled,center=10):
    km = TimeSeriesKMeans(n_clusters=center, metric="softdtw", max_iter=5, verbose=False, random_state=0).fit(data_scaled)
    return km

def exampleTSMeans(df,center=10,class1=0):
    data_scaled = get_normal_tslearn_data(df)
    km = TSKMeans(data_scaled,center)
    lab_1 = get_one_lable_index(km.labels_,class1)
    return lab_1