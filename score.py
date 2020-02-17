#!/usr/bin/python
# -*- coding: UTF-8 -*-

score=int(input("Please input your score:"))

if score >=0 and score < 60:
    print ("bujige")
elif  score >=60  and score < 85:
    print ("lianghao")
elif  score >=85 and score <=100:
    print ("good...")
else:
    print ("buhege.Error...")
