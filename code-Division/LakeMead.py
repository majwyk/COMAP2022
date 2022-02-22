import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_elevation = pd.read_csv('./LakeMeadPoolElevation(feet).csv')
file_storage = pd.read_csv('./LakeMeadStorage(acre-feet).csv')

lakeMead_elevation = np.expand_dims(pd.DataFrame(file_elevation)['pool elevation'].values, axis=1)
lakeMead_storage = np.expand_dims(pd.DataFrame(file_storage)['storage'].values, axis=1)

lakeMead = np.concatenate((lakeMead_elevation,lakeMead_storage),axis=1)
lakeMead = lakeMead[15558:,:]
lakeMead_sort = lakeMead[lakeMead[:, 0].argsort()] # 根据水位高度排序
# lakeMead_sort = lakeMead[lakeMead[22863:, 0].argsort()] # 根据水位高度排序

# 打印水位高度与储量不呈正相关的点
# for i in range(len(lakeMead_sort[:,0])-1):
#     if lakeMead_sort[i, 1] > lakeMead_sort[i+1, 1]:
#         print(i, lakeMead_sort[i,0], lakeMead_sort[i,1])
#         print(i+1, lakeMead_sort[i+1,0], lakeMead_sort[i+1,1])
#         print()

# 拟合曲线并画图
f1 = np.polyfit(lakeMead_sort[:,0], lakeMead_sort[:,1], 3)
print('f1 is :\n',f1)
yvals=np.polyval(f1, lakeMead_sort[:,0])
plot1 = plt.scatter(lakeMead_sort[:,0], lakeMead_sort[:,1], label='original values')
plot2 = plt.plot(lakeMead_sort[:,0], yvals, 'r',label='polyfit values')

plt.xlabel('pool elevation')
plt.ylabel('storage')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('Relation between pool elevation and storage of Lake Mead')
plt.show()
