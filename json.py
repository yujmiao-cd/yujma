#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return '%s : %d, %d' %(self.name, self.age, self.score)


s = Student('Tom',15, 85)
# print (s)
# print(s.__dict__)

# way 1  
jtext = json.dumps(s, default = lambda obj: obj.__dict__)
print(jtext)

# way 2
def s2d(s):
    return s.__dict__
jtext = json.dumps(s, default = s2d)
print(jtext)

def d2s(d):
    return Student(d['name'], d['age'], d['score'])
ds = json.loads(jtext, object_hook = d2s)
print(ds)
