class MaxStack:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if not self.max_items or item >= self.max_items[-1]:
            self.max_items.append(item)

    def pop(self):
        if not self.items:
            return None

        item = self.items.pop()
        if item == self.max_items[-1]:
            self.max_items.pop()

        return item

    def get_max(self):
        if not self.max_items:
            return None
        return self.max_items[-1]


"""
This implementation is similar to the MinStack implementation, except that the max_items stack is used to keep track of the maximum element, and the element is pushed to this stack if it is greater than or equal to the current maximum (which is the top element of max_items). The get_max method returns the current maximum element, which is the top element of the max_items stack.
Since all operations on a stack are O(1), this implementation has an O(1) time complexity for the get_max method.
"""
