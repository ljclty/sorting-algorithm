# -*- coding = utf-8 -*-
# @time:2021/1/30 11:03
# Author:ljc
# @File:快速排序.py
# @Software:PyCharm

import numpy as np
import time
import sys
sys.setrecursionlimit(1000000)


def quick_sort(data, start, end):

    if start >= end:
        return

    left = start
    right = end
    base_data = data[start]

    while left < right:
        while (left < right) and (data[right] >= base_data):  # 第一步，寻找右边比base_data小的数据，移动右边索引。
            right -= 1                                        # 往左移动一步。
        data[left] = data[right]                              # 第二步，将右边数据写到左边。
        while (left < right) and (data[left] <= base_data):   # 第三步，寻找左边比base_data大的数据，移动右边索引。
            left += 1                                         # 往右移动一步。
        data[right] = data[left]                              # 第四步，将左边数据写到右边。
    data[left] = base_data                                    # 将data_base数据归位到left=right中。

    # 递归base_data左右
    quick_sort(data, start, left-1)
    quick_sort(data, left+1, end)

if __name__ == '__main__':
    data = np.random.randint(1, 1000, 10000)
    data = data.tolist()
    print(data)
    start_time = time.time()
    quick_sort(data, 0, len(data)-1)
    print(data)
    print("快速排序耗时:", time.time() - start_time)


"""
快速排序总结：
一.
首先找到base_data,取左边第一个位置，start=0，end=len(data)；
索引j从右往左遍历，如果data[j]>=base_data，j -= 1；否则data[i] = data[j];
索引i从左往右遍历，如果data[i]<=base_data，i += 1；否则data[j] = data[i];
直到i=j=mid时，第一次结束，此时data[mid] = data_base;
然后，分别对[start,mid-1],[mid+1,end]进行递归；
二.
快速排序是不稳定排序！
三.
时间复杂度为:O(nlogn)
上述耗时0.02s左右！！！
"""