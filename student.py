#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
  
    def __init__(self, score=0):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value
        return self.__score

    @property
    def rate(self):
        if self.__score > 90:
            return 'A'
        else:
            return 'B' 


s = Student()
s.score = 70

print(s.score)
print(s.rate)
