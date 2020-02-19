#!/usr/bin/python
# -*- coding: UTF-8 -*-

def startPos(m,n):
    def newPos(x,y):
        print "The old position is (%d,%d), and the new position is (%d,%d)" %(m,n,m+x,n+y)
    return newPos


action = startPos(10,10)
action(3,4)
action(4,5)
