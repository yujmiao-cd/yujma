#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
匹配括号序列。
{[([])]}  True
{{[([]}}  False

'''



def isValidiParentheses(s):
    st = []
    for c in s:
        if ( c == '(' or c == '[' or c == '{' ):
            st.append(c)
        else :
            if not check(c, st):
                return False
    return True if not st else False

def check(c, st):
    # None  代表是空值
    if not st:
        return False
    lp = st[-1]
    if ( (lp == '(') and (c == ')') or \
         (lp == '{') and (c == '}') or \
         (lp == '[') and (c == ']') ):
        st.pop()
        return True
    else:
        return False

print(isValidiParentheses('{[([])]}'))
print(isValidiParentheses('{[([})]}'))

