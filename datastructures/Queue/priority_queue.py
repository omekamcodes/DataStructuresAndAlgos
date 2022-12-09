# Basic
class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)[0]

    def peek(self):
        if not self.items:
            return None

        return self.items[0][0]


"""
In this implementation, the PriorityQueue class has an items list that stores the items in the queue as tuples, where the first element of the tuple is the item and the second element is its priority. 
The enqueue method adds a new item to the list and sorts it according to the priorities. 
The dequeue and peek methods remove and return the first item in the list, respectively.

Note that this implementation has an O(n log n) time complexity for the enqueue, dequeue, and peek operations, 
since the list is sorted whenever an item is added or removed. There are other ways to implement a priority queue that have a better time complexity for these operations, 
such as using a binary heap instead of a list.
"""
