import numpy as np
import pandas as pd

drought = pd.read_csv('./五年干旱数据.csv')
drought.drop(labels='ValidStart', axis=1, inplace=True)
drought.drop(labels='ValidEnd', axis=1, inplace=True)
drought.drop(labels='StatisticFormatID', axis=1, inplace=True)
AZ = drought.loc[drought['StateAbbreviation']=='AZ']
CA = drought.loc[drought['StateAbbreviation']=='CA']
CO = drought.loc[drought['StateAbbreviation']=='CO']
NM = drought.loc[drought['StateAbbreviation']=='NM']
WY = drought.loc[drought['StateAbbreviation']=='WY']
drought_state = [AZ, CA, CO, NM, WY]
AZ_list = []
CA_list = []
CO_list = []
NM_list = []
WY_list = []
drought_list = [AZ_list, CA_list, CO_list, NM_list, WY_list]
stateName = ['AZ', 'CA', 'CO', 'NM', 'WY']

pos = 0
for state, l in zip(drought_state, drought_list):
    state.drop(labels='StateAbbreviation', axis=1, inplace=True)
    for i in range(pos, pos+len(state)):
        state['MapDate'][i] = str(state['MapDate'][i])[4:6]+'-'
    l.append(state.loc[state['MapDate'] == '01-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '02-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '03-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '04-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '05-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '06-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '07-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '08-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '09-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '10-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '11-'].drop(labels='MapDate', axis=1, inplace=False).values)
    l.append(state.loc[state['MapDate'] == '12-'].drop(labels='MapDate', axis=1, inplace=False).values)
    pos += len(state)

for l in drought_list:
    for i in range(len(l)):
        l[i] = np.mean(l[i], axis=0)

for name, l in zip(stateName, drought_list):
    print('\n{}'.format(name))
    for i in range(len(l)):
        sum = 0
        for d in range(1, 6):
            sum += 10**(d+0.45)*l[i][d]
        l[i] = sum
        print('{:2}月:\t{}'.format(i+1, l[i]))
