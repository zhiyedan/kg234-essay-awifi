# coding:utf-8
# 该模块用来画图
import pandas as pd
import matplotlib.pyplot as plt
import random
from bokeh.charts import TimeSeries
from bokeh.io import output_notebook, show
output_notebook()

# 给定的列里随机选择random_num列，画出
def plt_random_cols(df,cols_index,rand_col_num):
    rand_col = random.sample(df.columns[cols_index].values.tolist(),rand_col_num)
    data = df[rand_col]
    # plt.legend(loc="best")
    TOOLS = 'pan,wheel_zoom,crosshair,resize,reset,save'
    ts_plt = TimeSeries(data,title="time series",xlabel='time',ylabel='count',plot_width=900, plot_height=500,tools=TOOLS)
    show(ts_plt)
    
def plt_one_ts(ts):
    plt.legend(loc="best")
    TOOLS = 'pan,wheel_zoom,crosshair,resize,reset,save'
    ts_plt = TimeSeries(ts,title="time series",xlabel='time',ylabel='count',plot_width=900, plot_height=500,tools=TOOLS)
    show(ts_plt)