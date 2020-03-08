#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
随机产生 10 个数字，
要求：
每个数字的取值范围：[1, 20]
统计重复的数字有几个
统计不重复的数字有几个
'''

import random
'''
lst = []
rep = []
no_rep = []
count = 0
for i in range(10):
    lst.append(random.randint(1,10))
print(lst)
'''

same_nums = []   # 记录相同的数字
diff_nums = []   # 记录不同的数字
count = 0
nums = []
for _ in range(10):
    nums.append(random.randint(1,10))

length = len(nums)
states = [0] * length   # 记录不同的索引的异同状态

print("Origin numbers={}".format(nums))
print()

for i in range(length) :
    flag = False    #  假定没有重复值
    if states[i] == 1:
        continue
    for j in range(i+1, length):
        if states[j] == 1:
            continue
        if nums[i] == nums[j]:
            flag = True
            states[j] = 1
    if flag:  # 有重复
        same_nums.append(nums[i])
        states[i] == 1
    else:
        diff_nums.append(nums[i])

print("Same numbers = {1}, Count = {0}".format(len(same_nums), same_nums))
print("Different nums = {1}, COunt = {0}".format(len(diff_nums),diff_nums))

print(list(zip(states, nums)))




