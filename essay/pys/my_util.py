# coding:utf-8
import pandas as pd
import time
import datetime
import sklearn.metrics as metrics

def load_splited_data(file_path,col_is_time=True):
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'],unit='s')
    df = df.set_index('time')
    if col_is_time:
        df = df.T
    return df

def dt2time(dt):
    return dt.timetuple()

def time2ts(time_tuple):
    return time.mktime(time_tuple)

def get_1hour_data(col_is_time=False):
    return load_splited_data('../data/all_split_ts_1hour.csv',col_is_time)
    
def get_4month_data(col_is_time=False):
    return load_splited_data('../data/split_ts_4month.csv',col_is_time)

def time_decompose(raw_df,col_name='timestamp'):
    raw_df['datetime'] = pd.to_datetime(raw_df[col_name])
    raw_df['time'] = raw_df.datetime.apply(lambda x: x.timetuple())
    raw_df['timestamp'] = raw_df.time.apply(lambda x: int(time.mktime(x)))
    raw_df['hour'] = raw_df.time.apply(lambda x: x.tm_hour)
    raw_df['minute'] = raw_df.time.apply(lambda x: x.tm_min)
    raw_df.drop('time',axis=1,inplace=True)
    return raw_df

def metric(real_label, predict_label):
    precision = metrics.precision_score(real_label,predict_label)
    recall = metrics.recall_score(real_label, predict_label)
    f1score = metrics.f1_score(real_label,predict_label)
    conf_matrix = metrics.confusion_matrix(new_df.label, new_df.predict_label)
    print("precision:%.4f \nrecall: %.4f \nf1_score:%.4f " %(precision, recall,f1score))
    print("\nconfusion matrix:\n", conf_matrix)
    return conf_matrix
