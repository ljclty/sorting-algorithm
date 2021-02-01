# -*- coding = utf-8 -*-
# @time:2021/2/1 11:37
# Author:ljc
# @File:二分查找.py
# @Software:PyCharm

# 法一:使用递归！

import numpy as np
import time

def binary_search(data, num, left, right, k):

    if right >= left:

        mid = (left + right) // 2
        print("二分寻找第%i次:" % k, left, right, mid)

        if num == data[mid]:
            return "一共二分寻找{0}次,{1}在{2}位置" .format(k, num, mid)

        elif num < data[mid]:
            right = mid - 1
            k += 1
            return binary_search(data, num, left, right, k)

        else:
            left = mid + 1
            k += 1
            return binary_search(data, num, left, right, k)

    else:
        return None

if __name__ == "__main__":
    data = [1, 12, 15, 23, 25, 56, 77, 88, 110, 220, 1111]
    start_time = time.time()
    print(binary_search(data=data, num=0, left=0, right=len(data), k=1))
    print("二分查找耗时:", time.time() - start_time)


# 法二：使用while循环

def binary_search_2(data, num):
    left = 0
    right = len(data)
    k = 1

    while left < right:
        mid = (left + right) // 2
        print("第%i次二分查找" % k, left, right, mid)

        if num == data[mid]:
            return "二分查找一共{0}次,{1}在{2}位置".format(k, num, mid)

        elif num < data[mid]:
            right = mid - 1
            k += 1

        else:
            left = mid + 1
            k += 1
    else:
        return None

if __name__ == "__main__":
    data = [1, 12, 15, 23, 25, 56, 77, 88, 110, 220, 1111]
    start_time = time.time()
    print(binary_search_2(data=data, num=15))
    print("二分查找耗时:", time.time() - start_time)


"""
二分查找算法总结：
一.
二分法从数组的中间位置开始搜索，如果中间元素就是寻找元素，算法终止；
如果中间元素大于寻找元素，则在小于等于中间元素那一部分寻找；
如果中间元素小于寻找元素，则在大于等于中间元素那一部分寻找；
寻找条件是left<=right,如果寻找完没有找到元素，则返回None！
二.
二分查找时间复杂度为:o(log(n))
"""