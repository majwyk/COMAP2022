import numpy as np
import pandas as pd

np.seterr(divide='ignore')

data = pd.read_excel('./综合评价数据.xlsx')
# stateName = ['Arizona','California','Colorado','New Mexico','Wyoming']
stateName = ['Colorado','New Mexico','Wyoming']
print('月综合权重:(需求量, 依赖度, 干旱度)\n')
for month in range(1, 13):
    data_per_month = data.iloc[2+5*(month-1):5*month, 2:5].values
    max = data_per_month.max(axis=0)
    min = data_per_month.min(axis=0)
    data_per_month -= min
    data_per_month /= max - min

    p = data_per_month / data_per_month.sum(axis=0)
    test = p*np.nan_to_num(np.log(p))
    e = -1/np.log(len(stateName))*test.sum(axis=0)
    w = (1 - e) / np.sum(1 - e)
    print('{:2}月: {}'.format(month, w))

    data_per_month = data.iloc[2+5*(month-1):5*month, 2:5].values
    score = (data_per_month * w).sum(axis=1)
    percentage = score / score.sum()
    for state in stateName:
        print('\t{:11}: {:9.6f} %'.format(state, percentage[stateName.index(state)]*100))
    print()
