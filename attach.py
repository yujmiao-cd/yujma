#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Publisher:
    def __init__(self):
        self.observers = []
   
    def attach(self,observer):
        self.observers.append(observer)

    def notifyAll(self,msg):
        for o in self.observers:
            o.update(msg)


class ObserverA:
    def register(self,publisher):
        publisher.attach(self)

    def update(self,msg):
        print ("ObserverA: %s" % msg)

class ObserverB:
    def register(self,publisher):
        publisher.attach(self)

    def update(self,msg):
        print ("ObserverB: %s" % msg)

p = Publisher()
oa = ObserverA()
ob = ObserverB()
oa.register(p)
ob.register(p)
p.notifyAll('Hello...')
