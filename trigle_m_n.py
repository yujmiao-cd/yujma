#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
求杨辉三角第 n 行 第 k 列的值

求 m 行 k 个元素
m 行元素有 m 个， 所以 k 不能大于 m
这个需求需要保存 m 行的数据，可以使用一个嵌套机构 [[], [], []]
m = 5
k = 4
triangle = []
for i in range(m):
    # 所有行都需要 1 开头
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
print(triangle)
print("----------")
print(triangle[m-1][k-1])
print("----------")
'''
# m 行 k 列的值，C（m-1, k-1）组合数
m = 9
k = 5
# c(n, r) = n!/(r!(n-r)!)
# n 最大
n = m - 1
r = k - 1
d = n - r
targets = []   # r, n-r, n
factorial = 1

for i in range(1, n+1):
    factorial *= i
    if i == r:
        targets.append(factorial)
    if i == d:
        targets.append(factorial)
    if i == n:
        targets.append(factorial)

# print (targets)
print(targets[2]//(targets[0]*targets[1]))


