#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
n = 100
pn = []
count = 0

for x in range(2, n):
    for i in pn:
        count += 1  #  how many times
        if x % i == 0:
            break
    else:
        pn.append(x)
print(pn)
print(count)
