#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import re

s = '0123abcd'

regex = re.compile('[ab]')

# matcher = re.match('\d',s)   # 锚定索引开始 0
#
# print(type(matcher))
#
# print(matcher)
#
# matcher = regex.match(s, 4)   # 锚定索引开始的位置在第4个位置
#
# print(type(matcher))
#
# print(matcher)

# matcher = re.search('[ab]', s)
# print(type(matcher))
# print(matcher)
#
# matcher = regex.search(s)   # pos
# print(type(matcher))
# print(matcher)

matcher = re.fullmatch('\w+', s)
print(type(matcher))
print(matcher)

matcher = regex.fullmatch(s, 4, 5)
print(type(matcher))
print(matcher)

