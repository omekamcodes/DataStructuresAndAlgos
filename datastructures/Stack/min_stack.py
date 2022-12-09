class MinStack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        if not self.items:
            return None

        item = self.items.pop()
        if item == self.min_items[-1]:
            self.min_items.pop()

        return item

    def get_min(self):
        if not self.min_items:
            return None
        return self.min_items[-1]


"""
This implementation uses an additional stack, called min_items, 
to keep track of the minimum element. Each time a new element is pushed to the stack, 
it is also pushed to the min_items stack if it is less than or equal to the current minimum (which is the top element of min_items). 
When an element is popped from the stack, it is also popped from min_items if it is equal to the current minimum.

The get_min method returns the current minimum element, 
which is the top element of the min_items stack. Since all operations on a stack are O(1), 
this implementation has an O(1) time complexity for the get_min method.
"""
