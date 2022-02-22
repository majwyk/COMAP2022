#%%
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

powellin = pd.read_csv("lakepowell_release.csv")
powellin["datetime"] = pd.to_datetime(powellin["datetime"])
# %%
annualin = powellin.loc[0,"release volume"]

yearlist = []
annualinlist = []

# plt.plot(powellin['datetime'].tolist(),powellin['inflow volume'].tolist())
# plt.show()

# Sync the year data
for i in range(1,powellin.shape[0]):
    if powellin.loc[i,"datetime"].year == powellin.loc[i-1,"datetime"].year and powellin.loc[i,"datetime"].month == powellin.loc[i-1,"datetime"].month: 
        annualin+=powellin.loc[i,"release volume"]
    else:
        yearlist.append(str(powellin.loc[i-1,"datetime"].year)+"-"+str(powellin.loc[i-1,"datetime"].month))
        annualin+=powellin.loc[i-1,"release volume"]
        annualinlist.append(annualin/1000)
        annualin = powellin.loc[i,"release volume"]

final = pd.DataFrame({
    'date': yearlist,
    'release volume': annualinlist
})

print(final)
final.to_csv("lakepowell_monthlyrelease.csv",index=False)