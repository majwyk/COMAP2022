import numpy as np
import pandas as pd

population = pd.read_excel('./2010美国人口普查结果.xls').iloc[[12,14,15,41,60],:]
usage = pd.read_excel('./2010年美国用水情况.xlsx').iloc[[6,8,9,35,54],[0,14]]
population.columns = ['state', 'population']
stateName = population['state'].values.tolist()
population.index = stateName
population.drop(labels='state', axis=1, inplace=True)
usage.columns = ['state', 'usage']
usage.index = stateName
usage.drop(labels='state', axis=1, inplace=True)
need = {}
for state in stateName:
    need[state] = usage.loc[state].values.item()/(population.loc[state].values.item()/1000)
print('每千人人均需求量(thousand acre-feet):')
for n in need:
    print('{:12}:  {}'.format(n, need[n]))