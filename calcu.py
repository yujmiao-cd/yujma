#!/usr/bin/python
# -*- coding: UTF-8 -*-

# caculator

def calcurate(num1,num2,oper):
    if oper == "+":
        return x + y
    elif  oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    elif oper =='/':
        return x / y
    elif oper == '%': 
        return x % y
    elif oper == '**':
        return x ** y
    else:
        return False

if __name__ =='__main__':
    try:
        num1 = int(input("Please enter num1:"))
        num2 = int(input("Plz Enter num2:"))
        operator = str(input("Plz Enter oper:"))
        res =  calcurate(num1,num2,operator)
        if res == "None":
            print "Sorry. Sisi unkown..."
        else:
            print ("sum:",res)
    except Exception :
        print "system not well..."
