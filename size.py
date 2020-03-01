#!/usr/bin/python
# -*- coding: UTF-8 -*-
def human(size):
    units = ['', 'K', 'M', 'G', 'T', 'P' ]
    depth = 0
    while size >= 1000:
        size = size // 1000
        depth +=1
    return "{}{}".format(size,units[depth])

print(human(9999))
print(human(10000))
print(human(1000000))
