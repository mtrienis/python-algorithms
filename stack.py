# first in last out, last in first out
class Stack:

    # initialize list
    def __init__(self):
        self.stack = []

    # return the last element of the list as it wast last in
    def pop(self):
        return self.stack.pop()

    # add an element to the end of the list
    def push(self, element):
        self.stack.append(element)