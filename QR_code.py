#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
随机生成 500 个激活码，格式如下： XXXX -XXXX - XXXX - XXXX， 每一位是数字或者大写英文字母
'''

import random

def getCode():
    codes = []
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(4):
        seg = []
        for j in range(4):
            seg.append(s[random.randint(0,len(s)-1)]) 
        codes.append(''.join(seg))
    return '-'.join(codes)

for i in range(5):
    print (getCode())

