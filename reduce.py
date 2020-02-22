#!/usr/bin/python
# -*- coding: UTF-8 -*-

from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9]

print (reduce (lambda x, y: x+ y, numbers))


