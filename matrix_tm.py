#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Python内置数据结构（切片）
给定一个 3*3 方阵，求其转置矩阵

1  2  3             1  4
4  5  6   =====>    2  5
                    3  6

matrix = [ [1,2,3], [4,5,6] ]
# matrix = [[1,4], [2,5], [3,6]]
tm = []
count = 0

for row in matrix:
    for i, col in enumerate(row):
        if len(tm) <  i + 1:     # matrix 有 i 列就要为 t 创建 i 行
            tm.append([])
        tm[i].append(col)
        count += 1

print(matrix)
print(tm)
print(count)
'''

# 先开辟空间效率较高

matrix = [ [1,2,3], [4,5,6] ]

tm = [[0 for col in range(len(matrix))] for raw in range(len(matrix[0]))]
count = 0

for i, raw in enumerate(tm):
    for j, col in enumerate(raw):
        tm[i][j] = matrix[j][i]
        count +=1

print(matrix)
print(tm)
print(count)



