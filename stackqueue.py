from node import Node
from stack import Stack
from pprint import pprint

import unittest

# test class for the stack data structure
class TestStack(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.stack = Stack()

    def test_queue(self):

        self.stack.push('1')
        self.stack.push('2')
        self.stack.push('3')
        
        first = self.stack.pop()
        second = self.stack.pop()
        third = self.stack.pop()

        self.assertEqual(first,'3')
        self.assertEqual(second,'2')
        self.assertEqual(third, '1')

# runs the unit tests
if __name__ == '__main__':
    unittest.main()
