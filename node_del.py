#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
删除单链表的节点
'''
class Node:
    def __init__(self, val, _next = None):
        self.val = val
        self.next = _next

# 1-> 2-> 3-> 4-> 5
# 删除节点 3
# 1-> 2-> [3] -> 4-> 5
def deleteNode(node):
    if node.next is None:
        node = None
    else:
        p = node.next
        node.val = p.val
        node.next = p.next

def traverse(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    return '->'.join(vals)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

deleteNode(n3)
print(traverse(n1))
    
