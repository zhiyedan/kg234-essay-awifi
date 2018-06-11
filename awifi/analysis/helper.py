# coding:utf-8
import pandas as pd
import numpy as np
import time

# 24行的空dataframe
def gen_empty_df():
    df = pd.DataFrame(np.random.randn(24),columns=['tmp'])
    return df

# 扩充 hour特征
def time_feature(df):
    df['time'] = df.timestamp.apply(lambda x: time.localtime(x))
#     df['datetime'] = df.timestamp.apply(lambda x: datetime.datetime.fromtimestamp(x))
    df['hour'] = df.time.apply(lambda x: x.tm_hour)
    return df

# split 24 维数据
def get_split_ts(df,macs):
    result_df = gen_empty_df()
    for mac in macs:
        mac_df = df[df.ap_mac==mac]
        mac_df = time_feature(mac_df)
        grouped_mac = mac_df.groupby('hour')['count'].agg(sum)
        result_df[mac] = grouped_mac
    result_df.drop(columns='tmp',inplace=True)
    result_df = result_df.fillna(0)
    return result_df