#!/usr/bin/python
# -*- coding: UTF-8 -*-

#  判断年份是否闰年

def get_run(years):
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 ==0):
        print ("{}是闰年".format(years))
    else:
        print ("{}不是闰年" .format(years))

if __name__ == '__main__':
    for i in range(2000,2020):
        get_run(i)



