"""
Stack class in Python that implements the stack data structure
"""


class Stack:
    def __init__(self):
        # Underlying data structure (list)
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# Test Cases:

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
