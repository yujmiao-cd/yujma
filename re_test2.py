#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import re

s = '''bottle\nbag\nbig\napple'''

for x in enumerate(s):
    if x[0] % 8 ==0:
        print()
    print(x, end=' ')
print('\n')

# match 方法
print('---match---')
result = re.match('b', s)
print(1, result) # bottle
result = re.match('a', s)
print(2, result) # None
result = re.match('^a', s, re.M)  #  依然从头开始找，多行模式没有用
print(3, result)
result = re.match('^a', s, re.S) #  依然从头开始找
print(4, result)

# 先编译，然后使用正则表达式对象
regex = re.compile('a')
result = regex.match(s)
print(5, result)

result = regex.match(s, 15)
print(6, result) # apple
print()

# search  方法
print ('---search---')
result = re.search('a', s)
print(7, result)

'''

(0, 'b') (1, 'o') (2, 't') (3, 't') (4, 'l') (5, 'e') (6, '\n') (7, 'b') 
(8, 'a') (9, 'g') (10, '\n') (11, 'b') (12, 'i') (13, 'g') (14, '\n') (15, 'a') 
(16, 'p') (17, 'p') (18, 'l') (19, 'e') 

---match---
1 <re.Match object; span=(0, 1), match='b'>
2 None
3 None
4 None
5 None
6 <re.Match object; span=(15, 16), match='a'>

---search---
7 <re.Match object; span=(8, 9), match='a'>
'''
