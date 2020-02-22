#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
实现函数 f（n），返回一个函数f，f（x）= n * x 。（lambda 实现）
'''

def fn(n):
    return lambda x: n * x

f = fn(5)
print(f(100))   # 500

f = fn(10)
print(f(100))  # 1000
