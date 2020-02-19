#!/usr/bin/python
# -*- coding: UTF-8 -*-

def deco(func):
    def wrapper(x):
        print "Please say something..>"
        func(x)
        print "No zuo no die..."
    return wrapper

@deco
def show(x):
    print x

show("Hello,Mars")



