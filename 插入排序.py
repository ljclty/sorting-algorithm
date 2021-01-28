# -*- coding = utf-8 -*-
# @time:2021/1/28 11:19
# Author:ljc
# @File:插入排序.py
# @Software:PyCharm

import time
import numpy as np
# 法一.这个方法是错误的，因为插入排序不是直接data[i], data[i-1] = data[i-1], data[i]
# 如此交换，使得占用空间变大，更加耗时。
# 简而言之，插入排序，不是相邻元素交换！！！
data = np.random.randint(1, 1000, 10000)
# print("原始数据为:", data)

start_time = time.time()
for i in range(1, data.shape[0]):
    while (i - 1 >= 0) and (data[i-1] > data[i]):
        data[i], data[i-1] = data[i-1], data[i]
        i -= 1
    # print("第%i次插入排序" % i, data)
# print("插入排序最终结果:", data)
print("插入排序耗时:", time.time() - start_time)



# 法二.
data = np.random.randint(1, 1000, 10000)
# print("原始数据为:", data)

start_time_2 = time.time()
for i in range(1, data.shape[0]):
     tmp = data[i]   # tmp暂存数据，这里解释了法一的错误，插入排序不是相邻元素交换！这种方法使得速度更快。为什么？
     j = i - 1
     while (j >= 0) and (tmp < data[j]):
         data[j+1] = data[j]  # 交换位置
         j -= 1  # 依次比较
     data[j+1] = tmp   # 最小值放到第一个位置
     # print("第%i次插入排序" % i, data)
# print("插入排序最终结果:", data)
print("插入排序耗时:", time.time() - start_time_2)

""""

插入排序总结：按照升序
一.
插入排序每一步是将一个待排序数据，插入到已经排序好的序列中。
首先，初始化第1个数据，然后第2个数据与第1个比较，排序完成2个数据；
然后，第3个数据，插入到已经排好的前2个数据，插入方法是依次与第2个数据比较，如果data[1]<data[2]，直接把第3个数据放到位置3既可。否则，比较data[0]与data[2],进行排序。
依次进行，循环终止！
二.
注意：如果data[1]>data[2]，直接使用data[2] = data[1]，不要使用data[2], data[1] = data[1], data[2]!!!!!

"""