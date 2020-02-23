#!/usr/bin/python
# -*- coding: UTF-8 -*-

class MyClass:
    def __init__(self,val):
        self.__val = val
 
    def display(self,s):
        print '%s:%d' %(s, self.__val)

m = MyClass(100)
m.display('hello') 
print(m._MyClass__val)
m.__val=200
