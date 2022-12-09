"""
To implement a Queue class with O(1) time complexity for the dequeue and peek operations, 
we can use a doubly-linked list instead of a list. Here is an example:
"""


class Queue:
    class Node:
        def __init__(self, item, prev=None, next=None):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = self.Node(item, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None

        item = self.head.item
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return item

    def peek(self):
        if not self.head:
            return None

        return self.head.item


"""
In this implementation, the Queue class has a nested Node class that represents a node in the doubly-linked list. 
The enqueue method adds a new node to the end of the list, and the dequeue method removes the first node from the list. 
The peek method returns the item in the first node without removing it.

Since the doubly-linked list allows constant-time insertions and deletions at the beginning and end, 
this implementation has an O(1) time complexity for the enqueue, dequeue, and peek operations.
"""
