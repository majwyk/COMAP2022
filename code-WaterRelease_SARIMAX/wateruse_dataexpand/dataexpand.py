import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Load water usage
waterusage = pd.read_excel("5State_HistoricalWaterUse.xlsx","Data")
waterusage.sort_values("year",ascending=True,inplace=True)
waterusage = waterusage.reset_index(drop=True)
# print(waterusage)

# Data expand for states river demand
state_dict = ("AZ","CA","CO","NM","WY")
water_usage_ratio = (0.58211,0.13754,0.44553,0.12712,0.33077)

years = waterusage["year"].tolist()

yearlist = range(1985,2016)

final = pd.DataFrame({
    'year': yearlist,
})

# fit_s_dict = {
#     "AZ":5e10,
#     "CA":5e50,
#     "CO":5e10,
#     "NM":5e10,
#     "WY":5,
# }

for statename in state_dict:
    nowstate = waterusage[statename].tolist()
    print(years)
    print(nowstate)
    f = interpolate.UnivariateSpline(years,nowstate)
    statepredict = []
    for year in yearlist:
        statepredict.append(f(year))
    final[statename] = statepredict
    plt.plot(yearlist,statepredict)
    plt.plot(years,nowstate)
    plt.title(statename)
    plt.show()

print(final)
final.to_csv("LakeMeadMonthlyPoolElevation(feet).csv",index=False)