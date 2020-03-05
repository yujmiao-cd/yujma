#!/usr/bin/python3
# -*- coding: UTF-8

# 输入五个数字，打印每个数字的位数，讲三个数字排序打印，要求升序打印。
nums = []
while len(nums) < 5:
    num = input("Please input a number:").strip().lstrip('0')

    if not num.isdigit():
        continue

    print("The length of {} is {}".format(num, len(num)))
    nums.append(int(num))
print(nums)
