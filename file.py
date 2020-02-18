#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path

filename = '/kittod/yujma/file-1.txt'

if os.path.isfile(filename):
    f1 = open(filename,'a+')

while True:
    line = raw_input('Enter something...')
    if line == 'q' or line == 'Q':
        break
    f1.write(line+'\n')

f1.close()

