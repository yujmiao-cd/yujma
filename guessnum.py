#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

num = random.randint(1,101)

count = 0

while True:
   
# print ("your guessed times_count_new: ",count_new)
   mynum = int(input("Please input the num(1-100):"))
   count += 1
   
   if mynum < num:
       print ("small...")
   elif mynum > num:
       print ("big...")
   else:
       break
   
print ("your guessed times: ",count)

