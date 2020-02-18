#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = 6
z = "global"

def f1():
    x = "from f1"
    y = 3
    print x,z 
    def f2():
        x = "from f2"
        print x,y,z
    f2()

f1()

