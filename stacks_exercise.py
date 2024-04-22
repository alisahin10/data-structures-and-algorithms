""" Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial."""
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
from collections import deque


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

    def reverse_string(self, value):
        # Push each character of the string onto the stack
        for char in value:
            self.push(char)

        # Pop each character from the stack to reverse the order
        reversed_string = ''
        while not self.is_empty():
            reversed_string += self.pop()

        return reversed_string


s = Stack()
print(s.reverse_string('We will conquer COVID-19'))
