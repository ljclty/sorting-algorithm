# -*- coding = utf-8 -*-
# @time:2021/1/29 10:53
# Author:ljc
# @File:合并排序.py
# @Software:PyCharm

# 1.最简单形式
list1 = [1, 5, 8, 11, 14, 17]
list2 = [3, 4, 5, 6, 9, 15, 18, 20]

def merge(list1, list2):
    list = []
    i, j = 0, 0
    k = 1
    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            list.append(list1[i])
            i += 1
        else:
            list.append(list2[j])
            j += 1
        print("第%i次合并排序:" % k, list)
        k += 1
    # 将没有进行排序的直接添加到后面
    if i == len(list1):
        list.extend(list2[j:])
    else:
        list.extend(list1[i:])

    print("第%i次合并排序最终结果:" % k, list)
merge(list1, list2)


import numpy as np
import time

# 2.一般形式
start_time = time.time()
def merge_sort(lists):
    """
    递归进行合并排序
    """
    # 递归结束条件
    if len(lists) <= 1:
        return lists
    k = 1

    # 分治进行递归
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])

    # 将两个有序数组进行合并！！！这是重点
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        # 将最小的数据添加到result
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将没有参加到排序的数据，直接添加到后面
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    # print(result)
    return result

list = np.random.randint(1, 1000, 10000)
list = list.tolist()
print(merge_sort(lists=list))
print("合并排序耗时:", time.time() - start_time)



"""
合并排序总结：
一.
将一个序列从中间位置分为两个序列；
将这两个序列按照第一步继续二分；
直到子序列长度为1，不再分；
然后两两合并排序既可，按照选择排序进行！！！
二.
合并排序是稳定排序！
三.
时间复杂度为:O(nlogn)
上述耗时为0.04s左右！！！
"""