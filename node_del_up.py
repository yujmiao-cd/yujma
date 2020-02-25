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
def removeElement(head,val):
    prev, node = None,head
    while node:
        if node.val == val:
            if not prev:
                head = node.next
            else:
                prev.next = node.next
        else:
            prev = node
        node = node.next
    return head

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
n6 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
print(traverse(removeElement(n1,3)))
    
