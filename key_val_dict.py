#!/usr/bin/python
# -*- coding: UTF-8 -*-

l1=[0,1,2,3,4,5,6]

l2=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

j=0
count=0
dict = {}

for i in l1:
    # print i
     j = l2[count]
     count += 1
     dict.setdefault(i,j)

print dict
