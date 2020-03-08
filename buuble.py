#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
1. 从 lst = [1,(2,3,4),5] 中，提取4出来       lst[1][2]

In [16]: _,[*_,a],_=lst    print(a)

2. 环境变量 JAVA_HOME = /usr/bin ,返回变量名和路径

In [27]: s = 'JAVA_HOME=/use/bin'
In [28]: name,_,path = s.partition('=')
In [29]: name, path
Out[29]: ('JAVA_HOME', '/use/bin')

In [32]: name, *_, path = s.split('=')
In [33]: name, path
Out[33]: ('JAVA_HOME', '/use/bin')

3. 对列表 [1, 9, 8, 5, 6, 7, 4, 3, 2] 使用冒泡排序法排序，要求使用封装和解构来交换数据
In [38]: for i in range(9):
    ...:     for j in range(8-i):
    ...:         if lst[j] > lst[j+1]:
    ...:             lst[j], lst[j+1] = lst[j+1], lst[j]
    ...: print (lst)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

lst = [1, 9, 8, 5, 6, 7, 4, 3, 2]
for i in range(9):
    for j in range(9-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]    #  先封装再解构
print(lst)

for i in range(9):
    flag = True   #  没有交换过
    for j in range(9-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]    #  先封装再解构
            flag == False
        if flag == True:
            break
print(lst)



