# first in first out
class Queue:

    # initialize list
    def __init__(self):
        self.queue = []

    # add the element to the end of the list
    def enqueue(self, element):
        self.queue.append(element)

    # return the first element in the list as it was first in
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False