#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
n = 100
pn = []
count = 0
flag = False
for x in range(2, n):
    for i in pn:
        count += 1
        if x % i == 0:   # not prime
            flag = True
            break
        if i >= math.ceil(x ** 0.5):   # prime
            flag = False
            break
    if not flag:
        pn.append(x)
print(pn)
print(count)
