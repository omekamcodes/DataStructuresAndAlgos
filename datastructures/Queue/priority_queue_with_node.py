class PriorityQueueWithNode:
    class Node:
        def __init__(self, item, priority, prev=None, next=None):
            self.item = item
            self.priority = priority
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item, priority):
        new_node = self.Node(item, priority, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

        self.sort()

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

    def sort(self):
        curr = self.head
        items = []
        while curr:
            items.append(curr)
            curr = curr.next

        items.sort(key=lambda x: x.priority)

        for i in range(len(items) - 1):
            items[i].next = items[i + 1]
            items[i + 1].prev = items[i]

        self.head = items[0]
        self.tail = items[-1]


"""
In this implementation, the PriorityQueue class has a nested Node class that represents a node in the doubly-linked list. The enqueue method adds a new node to the end of the list and sorts it according to the priorities using the sort method. 
The dequeue and peek methods remove and return the first node in the list, respectively.

The sort method traverses the list and stores the nodes in a list, 
then sorts this list according to the priorities. 
Finally, it updates the prev and next pointers of the nodes in the sorted list to form a new doubly-linked list.

Note that this implementation has an O(n log n) time complexity for the enqueue, dequeue, and peek operations, 
since the list is sorted whenever an item is added or removed. There are other ways to implement a priority queue that 
have a better time complexity for these operations, such as using a binary heap instead of a list.
"""
