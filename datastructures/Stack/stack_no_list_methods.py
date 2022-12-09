# Stack class in Python that implements the stack data structure
# without calling methods on self.items
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items = self.items + [item]

    def pop(self):
        last_item = self.items[-1]
        self.items = self.items[:-1]
        return last_item

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


"""
This implementation is similar to stack.py, 
but instead of calling methods such as append() and pop() on self.items, 
it uses list concatenation and slicing to manipulate the list directly. 
For example, the push() method concatenates the current list
"""

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
