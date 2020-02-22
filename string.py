#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
对于给定的一个source 字符串和target 字符串
在 source 中找出 第一个 target 出现的位置。如果不存在，返回-1

'''

def strStr(source,target):
    if (source is None) or (target is None):
        return -1
    for i in range(len(source)-len(target)+1):
        if source[i:i + len(target)] == target:
            return i
    return -1


print(strStr('source','target'))
print(strStr('abcdabcdefg','bcd'))
