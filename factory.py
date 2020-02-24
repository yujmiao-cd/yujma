#!/usr/bin/python
# -*- coding: UTF-8 -*-

class USFactory:
    def make(self):
        print ("make in Us...")


class CNFactory:
    def make(self):
        print ("make in china...")

class Factory:
    factories = { 'us':USFactory(), 'cn':CNFactory()}
    
    @classmethod
    def createFactory(cls,country):
        if country in cls.factories:
            return cls.factories[country]
        else:
            return None

f1 = Factory.createFactory('us') 
f2 = Factory.createFactory('us') 
print (id(f1) == id(f2))
f3 = Factory.createFactory('cn')
f1.make()
f3.make() 
