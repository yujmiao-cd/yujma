#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pathlib import Path
import argparse
import datetime
import stat


def human(size):
    units = [' ', 'K', 'M', 'G', 'T', 'P' ]
    depth = 0

    while size >= 1000:
        size = size // 1000
        depth +=1
    return "{}{}".format(size,units[depth])


def showdir(path='.', all=False, detail=False, human=False):
    p = Path(path)
    for file in p.iterdir():
        if not all and str(file.name).startswith('.'):   #. 开头不打印  --all
            continue
        # -l
        if detail:
           st = print(file.stat())
           # -rw-r--r--. 1 root root 768 2月  29 16:59 log_analysis.txt
           h = st.st_size
           if human:
               h = human(st.st_size)
           yield (stat.filemode(st.st_mode), st.st_nlink, st.st_uid, st.st_gid, str(h),
                 datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S'), file.name)
        else:
            yield (file.name,)

def convert_mode(mode:int):
    modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
    modestr = bin(mode)[-9:] # '110 110 100 ; 664
    ret = ""
    for i, c  in enumerate(modestr):
        if c == '1':
            ret += modelist[i]
        else:
            ret += '-'
    return ret

# d - s p b l c
def convert_type(file:Path):
    ret = ""
    if file.is_symlink():
        ret = 'l'
    elif file.is_fifo():
        ret = 'p'
    elif file.is_socket():
        ret = 's'
    else:
        ret = '-'
    return ret



# ls [path] [-l] [-a]
parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list all files.') # 构造解析器
parser.add_argument('path',nargs='?', default='.', help='path help')  #  位置参数
parser.add_argument('-l', action='store_true')
parser.add_argument('-a','--all',action='store_true')
parser.add_argument('-h', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args(('/Users/angleyu/PYDemo/','-l'))
    parser.print_help()
    print('args = ', args)
#    print(args.path, args.l, args.h, args.all )
    for st in showdir(args.path, args.all, args.l, args.h):
        print(st)


