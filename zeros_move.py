#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给一个数组 nums，写一个函数将0 移动到数组的最后面，非0元素保持原数组顺序。
eg：
nums = [0,1,0,3,12]
nums = [1,3,12,0,0]
'''

def move_Zeros(nums):
    zeros = 0
    ret = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros +=1
        else:
            ret.append(nums[i])
    ret1 = ret
    for i in range(0,zeros):
        ret1.append(0)
    print (ret1)

nums = [0,1,0,3,12,0,4,7,0]
move_Zeros(nums)
