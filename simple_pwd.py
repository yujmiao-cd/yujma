#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
简化路径
/home/  ==> /home
/a/b/../../c/ ==> /c   
'''

def simplofyPath(path):
    dirs = path.split('/')
    new_path = []
    for _dir in dirs:
        if (_dir == '..') and new_path:
            new_path.pop()
        elif _dir and (_dir != '.'):
            new_path.append(_dir)
    return '/' + '/'.join(new_path)

print(simplofyPath('/home/'))
print(simplofyPath('/a/./b/../../c/'))


