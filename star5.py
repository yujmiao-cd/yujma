#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
   *            1      1      2n-1   3 
  ***           2      3             2
 *****          3      5             1
*******         4      7             0

'''
from __future__ import print_function
def printStar(count):
  
    for i in range(1,count+1):
        # space number: 
        space_num = count -i
        for j in range(0, space_num):
            print (" ", end="") 
        # * number
        star_num = 2 * i -1
        for j in range(0, star_num):
            print ("*", end="")
        # 换行
        print("")   


        
if __name__ == '__main__':
    printStar(20)
    printStar(10)




