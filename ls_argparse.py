#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from pathlib import Path
import argparse
import datetime
import stat

def listdir(path='.', all=False, detail=False, human=False):

    def _get_human(size):
        units = [' ', 'K', 'M', 'G', 'T', 'P']
        # units = " KMGTP"
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth +=1
        return "{}{}".format(size,units[depth])

    def _showdir(path='.', all=False, detail=False, human=False):
        p = Path(path)
        for file in p.iterdir():
            if not all and str(file.name).startswith('.'):   #. 开头不打印  --all
                continue
            # -l
            if detail:
               st = file.stat()
               # -rw-r--r--. 1 root root 768 2月  29 16:59 log_analysis.txt
               h = st.st_size
               if human:
                   h = _get_human(st.st_size)
               yield (stat.filemode(st.st_mode), st.st_nlink, st.st_uid, st.st_gid, str(h),
              datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S'), file.name)
            else:
                yield (file.name,)

    yield  from sorted(_showdir(args.path, args.all, args.l, args.h), key=lambda x: x[len(x)-1])

# ls [path] [-l] [-a]
parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list all files.') # 构造解析器
parser.add_argument('path',nargs='?', default='.', help='path help')  #  位置参数
parser.add_argument('-l', action='store_true')
parser.add_argument('-a','--all',action='store_true')
parser.add_argument('-h', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args(('/kittod/yujma/','-lha'))
    parser.print_help()
    print('args = ', args)

    for st in listdir(args.path, args.all, args.l, args.h):
        print(st)


'''
age: ls [-l] [-a] [-h] [path]

list all files.

positional arguments:
  path       path help

optional arguments:
  -l
  -a, --all
  -h
args =  Namespace(all=True, h=True, l=True, path='/kittod/yujma/')
('-rw-r--r--', 1, 0, 0, '12K', '2020-02-23 16:31:26', '.Ordinary_func.py.swp')
('drwxr-xr-x', 8, 0, 0, '185 ', '2020-03-03 11:36:01', '.git')
('drwxr-xr-x', 5, 0, 0, '4K', '2020-03-03 09:44:14', 'bak')
('-rw-r--r--', 1, 0, 0, '2K', '2020-03-03 21:02:01', 'ls_argparse.py')
('-rw-r--r--', 1, 0, 0, '2K', '2020-03-01 21:49:38', 'ls_log.py')
('-rw-r--r--', 1, 0, 0, '253 ', '2020-03-03 10:01:40', 'su_num.py')
('-rw-r--r--', 1, 0, 0, '381 ', '2020-03-03 10:25:34', 'su_num_new.py')
('-rw-r--r--', 1, 0, 0, '795 ', '2020-03-03 11:23:22', 'trigle.py')'drwxr-xr-x', 2, 501, 20, '64 ', '2020-02-29 15:19:07', 'test')

'''
