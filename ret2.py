#!/usr/bin/python3
# -*- coding: UTF-8 -*-
s = '''bottle\nbag\nbig\nable'''

regex = re.compile('b(?P<body>\w+)(?P<tail>e)')
#matcher = regex.search(s)
matchers = regex.finditer(s)
print(matchers)

for matcher in matchers:
    print(matcher.groups())
    print(matcher.group(0))
    print(matcher.group(1))
    print(matcher.group(2))
    print(matcher.groupdict())
    print('---------')
'''
<callable_iterator object at 0x101185050>
('ottl', 'e')
bottle
ottl
e
{'body': 'ottl', 'tail': 'e'}
---------
('l', 'e')
ble
l
e
{'body': 'l', 'tail': 'e'}
---------
'''

