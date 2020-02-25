#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pickle

d = {'Python':100, "Basic":70}

b = pickle.dumps(d)
dd = pickle.loads(b)
print(b)
print (dd)

