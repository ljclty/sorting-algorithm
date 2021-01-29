# -*- coding = utf-8 -*-
# @time:2021/1/28 22:52
# Author:ljc
# @File:希尔排序.py
# @Software:PyCharm

import numpy as np
import time

data = np.random.randint(1, 1000, 10000)
size = data.shape[0]

start_time = time.time()

k = 1   # 用于计数
jmp = size // 2  # 划分数不一定是2，可以取其他数

while jmp != 0:
    for i in range(jmp, size):
        tmp = data[i]  # 用来暂存数据，类似于插入排序
        j = i - jmp
        while (j >= 0) and (data[j] > tmp):  # 插入排序
            data[j + jmp] = data[j]
            j -= jmp
    jmp = jmp // 2
    print("第%i次希尔排序:" % k, data)
    k += 1
print("希尔排序耗时:", time.time() - start_time)

"""
希尔排序总结：
一.
希尔排序是插入排序的一种，是对直接插入排序的改进。、
对于n个数据，取小于n的整数gap（gap称为步长），所有距离为gap的倍数的记录放在同一组；
接着，对各组内的元素进行直接排序，这一次过完，每一个组内元素是有序的；
然后，减小gap的值，重复上述分组和插入排序；
当gap=1时，整个数据就是有序的，算法终止！
简而言之，希尔排序是对插入排序的改进，改进方法是分组，分组方法是按照gap进行！
二.
希尔排序是不稳定排序
三.
时间复杂度为：比O(n^2)好一些！！！
上述耗时1s左右！
"""