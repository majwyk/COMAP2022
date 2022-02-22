import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

ori_weight = [0.48713378, 0.26167948, 0.25118673]
ori_weight = np.array(ori_weight)
test_rate = [0.80, 0.90, 1.00, 1.10, 1.20]
stateName = ['Colorado','New Mexico','Wyoming']
data = pd.read_excel('./综合评价数据.xlsx')
for i in range(3):
    all = np.zeros((5, 3))
    for rate in test_rate:
        need = pd.read_excel('./2010年Colorado River取水情况.xlsx').iloc[2:5, [2,4]].values.sum(axis=1)*1000
        available = 3788
        print('参数{}, 扰动系数{}'.format(i+1, rate))
        weight = ori_weight.copy()
        weight[i] = ori_weight[i]*rate
        july_data = data.iloc[2+5*(7-1):5*7, 2:5].values
        score = (july_data * weight).sum(axis=1)
        priority = (score / score.sum())*100
        # min-max fairness权重标准化
        priority /= priority.min()
        for state in stateName:
            print('{:11}: {:9.6f}'.format(state, priority[stateName.index(state)]))
        print()
        done = False
        round = 1
        total = np.zeros(3)
        print('分配量/需求量:')
        while(not done):
            print('\t第{}轮'.format(round))
            priority[need==0] = 0
            available /= priority.sum()
            allocate = priority*available
            available = (allocate - need)
            available[available<0] = 0
            available = available.sum()
            need_pre = need.copy()
            need = need - allocate
            need[need<0] = 0
            total += need_pre - need
            for state in stateName:
                print('\t{:11}: {:<12.6f}/{:12.6f}  Total:{:12.6f}'.format(state, allocate[stateName.index(state)], need_pre[stateName.index(state)], total[stateName.index(state)]))
            if not(np.any(need)) or not(np.any(available)):
                done = True
            round += 1
        all[test_rate.index(rate)] = total
        print()
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(test_rate, all[:, 0], 'r-', label='Colorado')
    # ax.set_ylim(3262.04, 3262.095)
    # ax.ticklabel_format(useOffset=False)
    # ax.legend(loc=2)
    # ax.set_ylabel('Colorado State Allocation(thousand acre-feet)')
    # ax2 = ax.twinx()
    # for j in range(1, 3):
    #     ax2.plot(test_rate, all[:, j], label=stateName[j])
    #     ax2.set_ylim(240, 320)
    # ax2.legend(loc=1)
    # ax2.set_ylabel('Other States Allocation(thousand acre-feet)')
    # ax.set_xlabel("Perturbation Factor")
    # plt.show()
