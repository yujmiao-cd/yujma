#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1 ---- shitou
2 ---- jiandao
3 ---- bu
'''

import random

sys = random.randint(1,3)

while True:
   own = int(input("Please input shitou-1, jiandao-2, bu-3:"))
   print ("sys input:",sys)
   print ("your input:",own)
  
   if sys == own :
       print ("ow...nice,Tie")
       break
   else:
       if sys ==1 and own ==2 :
           print ("sys win...") 
           break
       elif sys ==1 and own ==3 :
           print ("own win...") 
           break
       elif sys ==2 and own ==1 :
           print ("own win...") 
           break
       elif sys ==2 and own ==3 :
           print ("sys win...") 
           break
       elif sys ==3 and own ==1 :
           print ("sys win...") 
           break
       elif sys ==3 and own ==2 :
           print ("own win...") 
           break
       else:
           print ("Please input 1-3:")
