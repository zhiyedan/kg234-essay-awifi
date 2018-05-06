# coding:utf-8
import pandas as pd

def load_splited_data(file_path,col_is_time=True):
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'],unit='s')
    df = df.set_index('time')
    if col_is_time:
        df = df.T
    return df

def get_1hour_data(col_is_time=False):
    return load_splited_data('../data/all_split_ts_1hour.csv',col_is_time)
    
def get_4month_data(col_is_time=False):
    return load_splited_data('../data/split_ts_4month.csv',col_is_time)



