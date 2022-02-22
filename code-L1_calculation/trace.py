#%%
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

powellin = pd.read_csv("Lake Powell 流入数据.csv")
waterusage = pd.read_csv("上下游用水数据 (Interim Report 1).csv",'\t')
powellin["datetime"] = pd.to_datetime(powellin["datetime"])
# %%

annualin = powellin.loc[0,"inflow volume"]

yearlist = []
annualinlist = []

# plt.plot(powellin['datetime'].tolist(),powellin['inflow volume'].tolist())
# plt.show()

# Sync the year data
for i in range(1,powellin.shape[0]):

    if powellin.loc[i,"datetime"].year == powellin.loc[i-1,"datetime"].year: 
        annualin+=powellin.loc[i,"inflow volume"]
    else:
        yearlist.append(powellin.loc[i-1,"datetime"].year)
        annualin+=powellin.loc[i-1,"inflow volume"]
        annualinlist.append(annualin/1000)
        annualin = powellin.loc[i,"inflow volume"]

yearlist_use = waterusage['year'].tolist()
waterusage = waterusage['upperwateruse'].tolist()


# plt.plot(yearlist,annualinlist)
# plt.plot(yearlist_use,waterusage)
# plt.show()
# %%
# Calculate total source water amount

source = []
for i in yearlist_use:
    source.append(annualinlist[yearlist.index(i)] + yearlist_use[yearlist_use.index(i)])

# 这个代码目前画的图象是源头总水量，但是样本数据过少，对于规律拟合效果差。目前忽略月度用水量差异，将用量差分开，使用ARIMA模型建模

plt.plot(yearlist_use,source)
plt.show()