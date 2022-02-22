import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_elevation = pd.read_csv('./LakePowellPoolElevation(feet).csv')
file_storage = pd.read_csv('./LakePowellStorage(acre-feet).csv')

lakePowell_elevation = np.expand_dims(pd.DataFrame(file_elevation)['pool elevation'].values, axis=1)
lakePowell_storage = np.expand_dims(pd.DataFrame(file_storage)['storage'].values, axis=1)

lakePowell = np.concatenate((lakePowell_elevation,lakePowell_storage),axis=1)
lakePowell_sort = lakePowell[lakePowell[:, 0].argsort()] # 根据水位高度排序

# 打印水位高度与储量不呈正相关的点
# for i in range(len(lakePowell_sort[:,0])-1):
#     if lakePowell_sort[i, 1] > lakePowell_sort[i+1, 1]:
#         print(i, lakePowell_sort[i,0], lakePowell_sort[i,1])
#         print(i+1, lakePowell_sort[i+1,0], lakePowell_sort[i+1,1])
#         print()

# 拟合曲线并画图
f1 = np.polyfit(lakePowell_sort[:,0], lakePowell_sort[:,1], 3)
print('f1 is :\n',f1)
yvals=np.polyval(f1, lakePowell_sort[:,0])
plot1 = plt.scatter(lakePowell_sort[:,0], lakePowell_sort[:,1], label='original values')
plot2 = plt.plot(lakePowell_sort[:,0], yvals, 'r',label='polyfit values')

plt.xlabel('pool elevation')
plt.ylabel('storage')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('Relation between pool elevation and storage of Lake Powell')
plt.show()
