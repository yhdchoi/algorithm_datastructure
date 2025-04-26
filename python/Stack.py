from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    # return and delete
    def pop(self):
        return self.container.pop()

    # return and not delete
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

