from node import Node
from queue import Queue
from pprint import pprint

import unittest

# test class for the queue data structure
class TestQueue(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.queue = Queue()

    def test_queue(self):

        self.queue.enqueue('1')
        self.queue.enqueue('2')
        self.queue.enqueue('3')
        
        first = self.queue.dequeue()
        second = self.queue.dequeue()
        third = self.queue.dequeue()

        self.assertEqual(first,'1')
        self.assertEqual(second,'2')
        self.assertEqual(third, '3')

# runs the unit tests
if __name__ == '__main__':
    unittest.main()
