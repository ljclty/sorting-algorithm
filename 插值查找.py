# -*- coding = utf-8 -*-
# @time:2021/2/2 10:19
# Author:ljc
# @File:插值查找.py
# @Software:PyCharm

import numpy as np
import time

# 法一:使用递归法！
def interpolation_search(data, num, left, right, k):

    mid = left + (right - left) * (num - data[left]) // (data[right] - data[left])
    print("插值寻找第%i次:" % k, left, right, mid)

    # 数列中不含寻找数据的情况
    if (left > right) or (data[left] > num) or (data[right] < num):
        return "插值寻找{0}次,数列中不存在{1}！".format(k, num)

    # 存在时候的寻找

    if data[mid] == num:
        return "插值寻找一共{0}次,在数列索引{1}位置找到{2}！".format(k, mid, num)

    elif data[mid] > num:
        mid = mid - 1
        k += 1
        return interpolation_search(data, num, left, mid, k)

    else:
        mid = mid + 1
        k += 1
        return interpolation_search(data, num, mid, right, k)

if __name__ == "__main__":
    data = np.sort(np.random.randint(1, 1000, 10000))
    start_time = time.time()
    print(interpolation_search(data=data, num=199, left=0, right=len(data)-1, k=1))
    print("插值排序耗时:", time.time() - start_time)


# 法二：使用while循环！
def interpolation_search_2(data, num):

    left = 0
    right = len(data) - 1
    k = 1

    while left < right:
        mid = left + (right - left) * (num - data[left]) // (data[right] - data[left])
        print("插值寻找第%i次:" % k, left, right, mid)

        if data[mid] == num:
            return "插值寻找一共{0}次,在数列索引{1}位置找到{2}！".format(k, mid, num)

        elif data[mid] > num:
            right = mid - 1
            k += 1

        else:
            left = mid + 1
            k += 1

    else:
        return "数列中不存在{0}！".format(num)

if __name__ == "__main__":
    data = np.sort(np.random.randint(1, 1000, 10000))
    start_time = time.time()
    print(interpolation_search_2(data=data, num=199))
    print("插值排序耗时:", time.time() - start_time)


"""
插值查找总结：
一.
插值查找是二分查找的进化版，主要区别是对于mid的求法不同。
二分查找mid=(left+right)//2，
插值查找是mid = left + (right - left) * (num - data[left]) // (data[right] - data[left])
这样主要考虑了数据是平均分布，更加合理！
二.
插值查找时间复杂度为:o(loglogn),一般情况快于二分查找,特别是寻找次数可能更少！

"""