#%%
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

powellin = pd.read_csv("LakeMeadPoolElevation(feet).csv")
powellin["datetime"] = pd.to_datetime(powellin["datetime"])
# %%
level_to_avg = []
level_to_avg.append(powellin.loc[0,"pool elevation"])

yearlist = []
annualinlist = []

# Sync the year data
for i in range(1,powellin.shape[0]):
    if powellin.loc[i,"datetime"].year == powellin.loc[i-1,"datetime"].year and powellin.loc[i,"datetime"].month == powellin.loc[i-1,"datetime"].month: 
        level_to_avg.append(powellin.loc[i,"pool elevation"])
    else:
        yearlist.append(str(powellin.loc[i-1,"datetime"].year)+"-"+str(powellin.loc[i-1,"datetime"].month))
        level_to_avg.append(powellin.loc[i-1,"pool elevation"])
        annualinlist.append(np.mean(level_to_avg))
        level_to_avg = [powellin.loc[i,"pool elevation"]]

final = pd.DataFrame({
    'date': yearlist,
    'pool elevation': annualinlist
})

print(final)
final.to_csv("LakeMeadMonthlyPoolElevation(feet).csv",index=False)