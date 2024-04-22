from collections import deque
"""
stack = deque()
stack.append("https:www.interviewer-project.site")
stack.append("https:www.interviewer-project.site/home")
stack.append("https:www.interviewer-project.site/admin")

print(stack)
"""

# Push will save the value inside the Stack. (In)
# Pop will remove the value inside the Stack. (Out)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s = Stack()
s.push(5)
print(s.peek())
s.pop()
print(s.is_empty())
s.push(12)
s.push(154)
s.push(1135)
print(s.peek())
print(s.size())