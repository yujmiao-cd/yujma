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
 *********         line  star     space
***********        6    11         0           2*5+2
 *********         7    9          1           2*4+1
  *******          8    7          2           2*3+1
   *****           9    5          3           2*2+1
    ***           10    3          4           2*1+1
     *            11    1          5           2*0+1

'''
from __future__ import print_function

count = 6
for i in range(1,count+1):
    # space number: 
    for j in range(0,count-i):
        print (" ", end="") 
    # * number
    for j in range(0,2*i-1):
        print ("*", end="")
    print("")   

for i in range(count-1, 0, -1):
    # space number:
    space_num =  count - i
    for j in range(1, space_num+1):
        print (" ", end="") 
    # * number
    start_num = 2 * i -1
    for j in range(1,start_num+1):
        print("*", end="")
    print("")

        





