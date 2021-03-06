# -*- coding: utf-8 -*-

class QueueNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        
class LinkedListQueue:
    def __init__(self):
        self.dummy = QueueNode(-1)
        self.tail = self.dummy
        
    def enqueue(self, val):
        node = QueueNode(val)
        self.tail.next = node
        self.tail = node
        
    def dequeue(self):
        if self.isEmpty():
            return -1
        ele = self.dummy.next.val
        self.dummy.next = self.dummy.next.next
        if not self.dummy.next:
            self.tail = self.dummy
        return ele
    
    def peek(self):
        return self.dummy.next.val
    
    def isEmpty(self):
        return self.dummy.next == None