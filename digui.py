#!/usr/bin/python
# -*- coding: UTF-8 -*-

# dihui 
'''
list = []
def fun1(n):
    
    if n <= 1:
        return n
    return fun1(n-1) + fun1(n-2)

for i in range(1,10):
    list.append(fun1(i))
print list
'''
# dizeng
'''
list = []
def fun2(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a+b
    return a 

for i in range(20):
    list.append(fun2(i))
print list
'''

# shengchengqi

list = []

def fun3(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
        yield a

for i in fun3(20):
    print i



