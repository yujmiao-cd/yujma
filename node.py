#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Node:
    def __init__(self,val=0, _next=None):
        self.val = val
        self.next = _next
    
    def traverse(head):
        vals = []
        while head:
            vals.append(str(head.val))
            head = head.next
        return '->'.join(vals)
    
    def reverse(head):
        if not head:
            return None
        new_head = None
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        return new_head
            
n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n1.next = n2
n2.next = n3
n3.next = n4
head = n1
print(traverse(head))
head = n1
head = reverse(head)
print(traverse(head))

