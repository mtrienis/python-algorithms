from node import Node
from search import Search
from pprint import pprint

import unittest

# test class for the triangle class
class TestDfs(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.a = Node('a')
        self.b = Node('b')
        self.c = Node('c')
        self.d = Node('d')
        self.e = Node('e')
        self.f = Node('f')
        self.g = Node('g')
        self.h = Node('h')

        #      a
        #    /   \
        #   b     c
        #  / \   / \
        # d   e f   g

        self.tree = {
                        'a': ['b','c'],
                        'b': ['d','e'],
                        'c': ['f','g'],
                        'd': [],
                        'e': [],
                        'f': [],
                        'g': []
        }

        #      10
        #    /   \
        #   4     7
        #  / \   / \
        # 3   5 6   8

        self.binary_tree = {
                        10: [4, 7],
                        4: [3, 5],
                        7: [6, 8],
                        3: [],
                        5: [],
                        6: [],
                        8: []
        }

        self.search = Search()

        
    def test_depth_first_search(self):
        print '---- depth first search ----'
        print self.search.depth_first_search(self.tree, 'a')


    def test_breadth_first_search(self):
        print '---- breadth first search ----'
        print self.search.breadth_first_search(self.tree, 'a')

# runs the unit tests
if __name__ == '__main__':
    unittest.main()
