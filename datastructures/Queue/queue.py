class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None

        return self.items[0]


""""
This implementation uses a list to store the items in the queue. 
The enqueue method adds an item to the end of the list, and the dequeue method removes an item from the beginning of the list. 
The peek method returns the item at the beginning of the list without removing it.

Note that this implementation has an O(n) time complexity for the dequeue and peek operations, 
since it involves shifting all the remaining items in the list by one position. 
There are other ways to implement a queue that have a better time complexity for these operations, 
such as using a linked list instead of a list.
"""
