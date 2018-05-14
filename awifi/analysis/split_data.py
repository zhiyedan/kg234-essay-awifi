# coding:utf-8
import pandas as pd
import time
import datetime

start_time = '2018/3/1'
end_time = '2018/5/1'

# str类型时间转为datatime
def str_2_datatime(str):
    return datetime.datetime.strptime(str,'%Y-%m-%d %H:%M:%S')

# str类型时间转为timestamp
def string_2_timestamp(time_str):
    return int(time.mktime(time.strptime(time_str,'%Y/%m/%d')))

# 过滤时间，默认为 2018/2/1-2018/4/1 零点
def filter_date(df,start_time=start_time,end_time=end_time):
    start_time = string_2_timestamp(start_time)
    end_time = string_2_timestamp(end_time)
    df =df[(df.time>=start_time) & (df.time<end_time)]
    return df

# 过滤掉数量太少的ap
def filter_count(df,count=100):
    # 自带升序
    mac_count = pd.Series(df.ap_mac).value_counts()
    filted_mac = list(mac_count[mac_count>count].index)
    query = "ap_mac in ("+",".join(["'"+x+"'" for x in filted_mac])+")"
    return df.query(query)

def timestap_date(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    return time.strftime(format,value)

def get_full_time_df(start_time=start_time,end_time=end_time,freq='H'):
    all_time = pd.date_range(start_time,end_time, freq=freq)
    full_time_df = pd.DataFrame(data={'time': all_time})
    return full_time_df

# df拆分为每个mac的时间序列
def split_merge_ts(df,full_time_df):
    ap_macs = df.ap_mac.unique()
    for mac in ap_macs:
        cur_df = df[df.ap_mac == mac].loc[:,['time','count']]
        merge_df = pd.merge(full_time_df,cur_df,how='left')
        merge_df = merge_df.rename(columns={'count':mac})
        full_time_df = merge_df
    full_time_df.fillna(0,inplace=True)
    return full_time_df

def split_df_to_ts(df):
    df['time'] = pd.to_datetime(df['time'], unit='s')
#    df['time'] = df.time.apply(timestap_date)
    full_time_df =  get_full_time_df()
    splited_df = split_merge_ts(df,full_time_df)
    splited_df = splited_df.set_index('time')
    return splited_df

if __name__ == '__main__':
    df = pd.read_csv('../data/awifi-zhongxintong-4month-data.log',sep='\t',header=None,names=['ap_mac','time','count'])
    df = filter_date(df)
    df = filter_count(df)
    df = split_df_to_ts(df)
    df.to_csv('../data/all_4month_log.csv')
    