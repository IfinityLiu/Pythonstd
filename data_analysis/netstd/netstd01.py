# -*- coding:utf-8 -*-
# Author: Infinity
# Create_time:2019-05-16 20:24:45

# %% 面向过程的图表
import numpy as np
import pandas as pd
from pyecharts.charts import Bar

# %% 做数据图表
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
x = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']

# %% 
bar = (
    Bar().add_xaxis(x)
    .add_yaxis('商家A',v1)
)
bar.render_notebook()