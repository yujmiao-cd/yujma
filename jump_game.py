#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
跳跃游戏，给出一个非负整数数组，你最初定位在数组的第一个位置。
跳跃数组中的每个数字代表你所能跳跃的最大长度。。
判断你是否能到数组的最后一个位置，A=  [2, 3, 1, 1, 4],返回 True
B = [3, 2, 1, 0, 4]  False
'''

def jump_game(A):
    '''
    1. 如果我当前能到k点，那我一定能到比k小的点。 x -> k [x+1, k-1]
    
    '''
    if not A:
        return False
    idx = len(A) - 1
    for i in range(len(A)-1, -1, -1):
        if (i + A[i]) >= idx:      # 代表可以从 i 点 到  idx 点
            idx = i 
    return idx == 0
'''
1. i=4,  idx = 4,  A[4] = 4 => idx =4
2. i=3,  idx = 4,  A[3] = 1 => idx =3
3. i=2,  idx = 3,  A[2] = 1 => idx =2
4. i=1,  idx = 2,  A[1] = 3 => idx =1
5. i=0,  idx = 1,  A[0] = 2 => idx =0  
'''

print(jump_game([2, 3, 1, 1, 4]))
print(jump_game([3, 2, 1, 0, 4]))

