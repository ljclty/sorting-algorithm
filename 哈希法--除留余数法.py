# -*- coding = utf-8 -*-
# @time:2021/2/3 10:38
# Author:ljc
# @File:哈希法--除留余数法.py
# @Software:PyCharm

import numpy as np
import time

# 除留余数法建立哈希表，如果发生碰撞，使用线性探测法储存数据！
def divide_remain(data, s, b):
    index = [None] * s
    for i in range(0, len(data)):
        remainder = data[i] % b
        while True:
            if index[remainder] is None:
                index[remainder] = data[i]
                print(data[i], "——>>", index)
                break
            else:
                remainder = (remainder + 1) % b
                print(data[i], "——>>", index)
    return "除留余数法最终储存结果为:{0}.".format(index)


if __name__ == "__main__":
    data = [1, 12, 11, 13, 14, 17, 21, 22, 24, 25, 333]
    start_time = time.time()
    print(divide_remain(data=data, s=len(data) + 100, b=111))
    print("除留余数法构造哈希表储存数据耗时为:", time.time() - start_time)

"""
哈希法总结：
一.
哈希法是利用哈希函数来计算一个键值所对应的地址，进而建立哈希表格，
然后利用哈希函数来寻找各个键值存在表格中的位置，查找速度与速度无关，
在没有碰撞与溢出时，一次读取既可找到指定数据位置。
二.
如果哈希函数f(num)=index，如果num1不等于num2，但是f(num1)=f(num2)就会发生溢出，发生碰撞！
三.
使用哈希算法寻找数据，时间复杂度为o(1),上述只是建立哈希表。
"""
