#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Python内置数据结构（切片）
给定一个 3*3 方阵，求其转置矩阵

1  2  3             1  4  7
4  5  6   =====>    2  5  8
7  8  9             3  6  9

===========1=============
# a[i][j] = a[j][i]

s = [[1,2,3], [4,5,6], [7,8,9]]

t = [[],[],[]]

for i in range(3):
    for j in range(3):
        if i != j:
            t[i].append(s[j][i])
        if i == j:
            t[i].append(s[i][j])
print(s)
print(t)

===========2=============
s = [[1,2,3,4], [5,6, 7,8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(s)):
    for j in range(i):
        s[i][j], s[j][i] = s[j][i], s[i][j]

print(s)
'''

matrix = [[1,2,3], [4,5,6], [7,8,9]]
count = 0
print(matrix)

for i, raw in enumerate(matrix):
    for j, col in enumerate(raw):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1

print(matrix)
print(count)








