#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给一个数组 nums，写一个函数将0 移动到数组的最后面，非0元素保持原数组顺序。
eg：
nums = [0,1,0,3,12]
nums = [1,3,12,0,0]
i = 0, nums[0] = 0,zeros = 1
i = 1, nums[1-1] = nums[1] , [1, 0, 0, 3, 12]  
'''

def move_Zeros(nums):
    zeros = 0
    for i in range(len(nums)):
        nums[i-zeros] = nums[i]
        if nums[i] == 0:
            zeros += 1
    for i in range(zeros):
        nums[len(nums) -i -1] =0
            

nums = [0,1,0,3,12,0,4,7,0]
move_Zeros(nums)
print nums
