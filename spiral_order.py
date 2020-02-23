#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给定一个包含 m * n 个要素的矩阵（m 行n 列）按照螺旋顺序，返回该矩阵中的所有元素。
[
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
]
打印输出：
[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

def spiralOrder(matrix):
    ret = []
    rows = len(matrix)
    if rows == 0:
        return ret
    columns = len(matrix[0])
    i, j = 0, 0 # 第一行第一列开始
    while (rows > 0) and (columns > 0):
        for k in range(j, j+columns):
            ret.append(matrix[i][k])
        if rows > 1:
            for k in range(i+1, i+rows):
                ret.append(matrix[k][j+columns -1])
            if columns > 1:
                for k in range(j + columns -2,j -1,-1):
                    ret.append(matrix[i+ rows-1][k])
                for k in range(i + rows - 2, i, -1):
                    ret.append(matrix[k][j])
        rows -= 2
        columns -= 2
        j +=1
        i += 1
    return ret

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralOrder(m))
 
