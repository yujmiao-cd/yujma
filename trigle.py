#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
杨辉三角：前六行
                 1                  n = 0
              1     1               n = 1
          1      2     1            n = 2
       1     3     3     1          n = 3
     1    4     6     4     1       n = 4
   1   5    10     10     5   1     n = 5

'''
trigle = []
n = 6
for i in range(n):    #  0 1 2 3 4 5
    row = [1]  #  开始的1
    for k in range(i):   # 中间填 0 尾部填 1    i=1
        row.append(1) if k == i - 1 else row.append(0)
    trigle.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1):   # i =3  可进入
        val = trigle[i-1][j-1] + trigle[i-1][j]
        row[j] =val
        if j != i-1: # 奇数个数的中间点去掉
            row[-j-1] = val
print(trigle)

