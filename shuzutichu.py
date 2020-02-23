#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
数组剔除之后的乘积
B[i] = A[0] * .. * A[i-1] * A[i+1] * ...* A[n-1],
eg:
A[1,2,3]  ==>  B[6,3,2] 
'''

def product(A):
    print (A)
    ret = [1] * len(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                ret[i] *= A[j]
    return ret

print(product([1,2,3,4]))
