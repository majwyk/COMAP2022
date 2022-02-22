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

sep_index = 414
powellin = powell.iloc[:sep_index,:]
powell_predict = powell.iloc[sep_index:-1,:]
# 这个是画上游总水量的总图

# fig = powellin.plot()
# plt.xlabel("Time(YYYY-mm)")
# plt.ylabel("Total water volume (kaf)")
# plt.title("Analysis of upper basin total water produce data")
# plt.show()


# ACF analysis
# fig = plt.figure(figsize=(12,6))
# ax1=fig.add_subplot(121)
# fig = sm.graphics.tsa.plot_acf(powellin,lags=20,ax=ax1)
# ax2 = fig.add_subplot(122)
# fig = sm.graphics.tsa.plot_pacf(powellin,lags=20,ax=ax2)
# plt.show() # ACF和PACF图，衡量数据中关系的

# ADF analysis
# It can be seen from the results that the model data itself meets the stability requirements
temp = np.array(powellin["inflow"])
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

# SARIMAX fit
from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(powellin, order=(8,1,4), seasonal_order=(1, 1, 1, 12))

result = model.fit()
print("fitresult:",result.aic,result.bic,result.hqic)

predict = result.predict()
# print(result.summary())

predictions = pd.Series(result.fittedvalues, copy=True)
print("R^2 is:",rsquare(predictions.tolist(),powellin["inflow"].tolist()))


prenew = predictions.to_frame()
prenew.reset_index(inplace=True)
prenew["date"] = pd.to_datetime(prenew["date"])
prenew = prenew.set_index("date",drop=True)

powellin.reset_index(inplace=True)
powellin["date"] = pd.to_datetime(powellin["date"])
powellin = powellin.set_index("date",drop=True)

# plt.figure(figsize=(15, 6))
# plt.plot(prenew,label="forecast")
# plt.plot(powellin,label="ground truth")
# plt.xlabel("Year")
# plt.ylabel("Total water volume (kaf)")
# plt.title("Model fit situation of current data")
# plt.legend()
# plt.show() # 画的是对源数据的拟合图

# 这个是预测后面12个月，并与真实标准比较
forecasted = result.forecast(12).tolist()
gt4predict = powell_predict["inflow"].tolist()[:12]
plt.figure(figsize=(15, 6))
plt.plot(forecasted,label="forecast")
plt.plot(gt4predict,label="ground truth")
plt.xlabel("Months in future")
plt.ylabel("Total water volume (kaf)")
plt.title("Model forecast of future in comparison with ground truth")
plt.legend()
plt.show()