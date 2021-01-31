# -*- coding = utf-8 -*-
# @time:2021/1/31 10:08
# Author:ljc
# @File:基数排序.py
# @Software:PyCharm

import numpy as np
import time

def radix_sort(data):
    degree = len(str(max(data)))                           # 计算最大的数字是几位数
    for i in range(0, degree):                             # 循环排序次数
        list = [[] for j in range(10)]                     # 生成10个桶，因为每位数，都是0-9
        for k in data:
            list[(k // 10**i) % 10].append(k)              # 每个位数，数字是几就添加到第几个桶

        data = [m for n in list for m in n]                # 对每一次排序后的结果进行去桶操作，并把数据更新！
        print("第%i次基数排序:" % i, data)

# radix_sort(data=[667, 810, 195, 338, 68, 787, 138, 203, 691, 8])

if __name__ == "__main__":
    data = np.random.randint(1, 1000, 10000)
    start_time = time.time()
    radix_sort(data=data)
    print("基数排序耗时:", time.time() - start_time)

"""
基数排序总结:
一.
首先对于个位数分桶排序0-9十个桶，更新数据；
然后对于十位数分桶排序0-9十个桶，更新数据；
如此循环，直到最大位数排好未知，终止！
二.
基数排序是稳定排序
三.
基数排序时间复杂度为:O(d(n+r))
上述耗时0.03s左右！！！
"""