#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy

l1=input("please input a list[num] :")

l1.reverse()

l2=copy.copy(l1)

for i in l2:
    print i

print "list reverse over..."

