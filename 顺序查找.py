# -*- coding = utf-8 -*-
# @time:2021/2/1 10:21
# Author:ljc
# @File:顺序查找.py
# @Software:PyCharm

import numpy as np
import time

def linear_search(data, number):
    find = 0
    for i in range(0, len(data)):
        if data[i] == number:
            print("在索引第{0}个位置找到{1}".format(i, number))
            find += 1
            # return i

    if find == 0:
        print("没有找到:", number)

if __name__ == "__main__":
    # data = np.random.randint(1, 10000, 10000)
    # data = data.tolist()
    data = [12, 23, 1, 15, 68, 77]
    start_time = time.time()
    linear_search(data=data, number=15)
    print("耗时:", time.time() - start_time)


"""
顺序查找算法总结：最简单的查找方法！
一.
顺序查找算法从第一个位置开始查找，从头到尾依次遍历，找到与目标相同的数的位置！
二.
时间复杂度为:O(n)
三.
我没有理解清楚是找到第一个形同的数，还是所有的形同的数的位置！！！
"""