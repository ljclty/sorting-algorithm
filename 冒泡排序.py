# -*- coding = utf-8 -*-
# @time:2021/1/28 11:15
# Author:ljc
# @File:冒泡排序.py
# @Software:PyCharm

import time
import numpy as np

# 法一
data = np.random.randint(1, 1000, 10000)
size = data.shape[0]
print("冒泡排序，原始数据为:", data)

start_time = time.time()
for i in range(size-1, -1, -1):  # 从右向左索引
    for j in range(0, i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
    # print("第%i次冒泡排序结果:" % (8-i), data)
print("冒泡排序最终结果:", data)
print("冒泡排序耗时:", time.time() - start_time)

# 法二
data = np.random.randint(1, 1000, 10000)
size = data.shape[0]
print("冒泡排序，原始数据为:", data)

start_time_2 = time.time()
for i in range(0, size):
    for j in range(0, size-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
    # print("第%i次冒泡排序结果:" % i, data)
print("冒泡排序最终结果:", data)
print("冒泡排序耗时:", time.time() - start_time_2)


"""
冒泡排序总结：
一.
从第一个数据开始比较相邻的数据，如果左边数据大于相邻右边数据，换位置；
第一次排序后，最右边得到最大数据；
按照上述，从第一个数据依次进行；
直到循环遍历完毕，终止！
二.
冒泡排序是一种稳定排序，如[1, 2, 1, 3]
第一次排完为[1, 1, 2, 3]，两个1的相对位置不会因为排序而改变。
三.
时间复杂度为O(n^2)
法一上述耗时25s左右
法二上述耗时26s左右
"""