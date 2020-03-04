#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
def calculate(args):
    operation = args.operation
    x = args.x
    y = args.y
    if "add" == operation:
        return x + y
    elif "sub" == operation:
        return x - y
    elif "div" == operation:
        return x / y 
    elif "mul" == operation:
        return x * y

def main():
    parse = argparse.ArgumentParser() 
    parse.add_argument("--x", type=float, default=1.0, help="what is the first number.")  
    parse.add_argument("--y", type=float, default=1.0, help="what is the second number.")   
    parse.add_argument("--operation", type=str, help="What operation? [add,mod,sub,div,mul]")
    args = parse.parse_args() 
    print(args)
    print(calculate(args))

main()

# https://www.cnblogs.com/freshchen/p/11660046.html
