#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from datetime import datetime

import statsmodels.api as sm     #acf,pacf图
from statsmodels.tsa.stattools import adfuller  #adf检验
from pandas.plotting import autocorrelation_plot
# from statsmodels.tsa.arima.model import ARIMA  


plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号

powellin = pd.read_csv("Lake Powell 流入数据.csv",index_col='datetime')
# powellin = powellin.drop(["datetime"],axis=1)
# powellin["datetime"] = pd.to_datetime(powellin["datetime"])
print(powellin.head())

fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(powellin,lags=20,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(powellin,lags=20,ax=ax2)
plt.show()

# 数据自相关检验
temp = np.array(powellin["inflow volume"])
print(temp)
t = adfuller(temp)  # ADF检验
output=pd.DataFrame(index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used","Critical Value(1%)","Critical Value(5%)","Critical Value(10%)"],columns=['value'])
output['value']['Test Statistic Value'] = t[0]
output['value']['p-value'] = t[1]
output['value']['Lags Used'] = t[2]
output['value']['Number of Observations Used'] = t[3]
output['value']['Critical Value(1%)'] = t[4]['1%']
output['value']['Critical Value(5%)'] = t[4]['5%']
output['value']['Critical Value(10%)'] = t[4]['10%']
print(output)

# # 此时模型满足平稳性要求，开始做ARIMA拟合

# powellin_dif1= powellin["inflow volume"].diff(1)
# plt.figure(figsize=(10, 6))
# powellin_dif1.plot()
# plt.xlabel('Date',fontsize=12,verticalalignment='top')
# plt.ylabel('Inflow Volume Diff1',fontsize=14,horizontalalignment='center')
# plt.show()

# model = sm.tsa.arima.ARIMA(powellin,order=(1,1,1))

# result = model.fit()

# predict = result.predict()
# print(result.summary())

# #%%

# predictions = pd.Series(result.fittedvalues, copy=True)
# print(predictions.head())

# plt.figure(figsize=(10, 6))
# plt.plot(predictions,label="forecast_diff")
# plt.plot(powellin,label="diff")
# # plt.xlabel('日期',fontsize=12,verticalalignment='top')
# # plt.ylabel('销量差分',fontsize=14,horizontalalignment='center')
# plt.show()
# %%
