# -*- coding = utf-8 -*-
# @time:2021/1/28 11:16
# Author:ljc
# @File:选择排序.py
# @Software:PyCharm

import numpy as np
import time

data = np.random.randint(1, 1000, 10000)
size = data.shape[0]
print("原始数据为:", data)

start_time = time.time()

for i in range(0, size):
    for j in range(i+1, size):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
    print("第%i次选择排序:" % i, data)
print("选择排序最终结果:", data)
print("选择排序耗时:", time.time() - start_time)

"""
按照升序排列总结：
一.
选择排序首先找到所有数据的最小值，放在首位；
其次在剩余数据中找到最小值，放在排序后的末尾；
依此进行；
直到所有数据排序完毕，终止！
二.
选择排序是一种不稳定的排序方式，如[2, 3, 2, 1]
第一次排序后为[1, 2, 3, 2],两个相等的数2相对位置改变，所以是不稳定排序。
三.
时间复杂度为:O(n^2)
上述耗时17s左右
"""