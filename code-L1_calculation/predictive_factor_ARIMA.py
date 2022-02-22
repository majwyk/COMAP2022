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

powell = pd.read_csv("Lake Powell 流入数据.csv",index_col='datetime')
powellin = powell.iloc[:14000,:]
print(powellin.size)

model = sm.tsa.arima.ARIMA(powellin,order=(3,1,1))

result = model.fit()

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
forecast = result.forecast(1000)
# predictions = pd.Series(forecast.fittedvalues, copy=True)

print(forecast)