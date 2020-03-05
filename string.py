#!/usr/bin/python3
# -*- coding: UTF-8 -*-
num = ""
while True:
    num = input("Please input a num:").strip().lstrip('0')
    if num.isdigit():
        num = str(num)
        break
    else:
        print("Not normal number ~ ")

count = [0]*10   # 0-9

for i in range(10):
    count[i] = num.count(str(i))

for i in range(10):
    if count[i]:
        print("{} 出现的次数是 {} 次.".format(i,count[i]))

lst = list(num)
lst.reverse()
print(" 列表反转的结果是 {}:".format(lst))
