#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
   *            1      1      2n-1   3 
  ***           2      3             2
 *****          3      5             1
*******         4      7             0




         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
'''
from __future__ import print_function

count = 10
for i in range(1,count+1):
    # space number: 
    for j in range(0,count-i):
        print (" ", end="") 
    # * number
    for j in range(0,2*i-1):
        print ("*", end="")
    print("")   

