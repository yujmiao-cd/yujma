#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = 30

def printInfo():
    print x + 30

class MyClass():
    
    data = "Hello, It's my module."
    
    def __init__(self,who):
        self.name=who

    def printName(self):
        print self.data,self.name

if __name__ == '__main__':
    printInfo()
    ins = MyClass('Jerry')
    print ins.name
    print ins.data
