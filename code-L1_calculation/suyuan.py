import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm     #acf,pacf图
from statsmodels.tsa.stattools import adfuller  #adf检验

# R^2 goodness of fit calculation
def rsquare(fit,original):
    res_ydata  = np.array(original) - np.array(fit)
    ss_res     = np.sum(res_ydata**2)
    ss_tot     = np.sum((original - np.mean(original))**2)
    r_squared  = 1 - (ss_res / ss_tot)
    return r_squared

# Processing the original data
# powellin = pd.read_csv("Lake Powell 月度数据.csv",index_col='date')
powell = pd.read_csv("Lake Powell MonthlyIn (1971-2008).csv",index_col='date')
# Add the upper basin water usage data
upperusage = pd.read_csv("上下游用水数据 (Interim Report 1).csv",sep='\t',index_col="year")["upperwateruse"]
for i in range(0,powell.size):
    powell.iloc[i]+= (upperusage[int(powell.iloc[i].name.split("-")[0])]/12)

powell.to_csv("Upper Total water production.csv")