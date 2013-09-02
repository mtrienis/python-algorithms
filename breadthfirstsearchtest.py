from breadthfirstsearch import BreadthFirstSearch

import unittest

# test class for the triangle class
class TestBreadthFirstSearch(unittest.TestCase):

    @classmethod
    def setUpClass(self):


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

        self.search = BreadthFirstSearch()

        

    def test_breadth_first_search(self):
        print '---- breadth first search ----'
        print self.search.breadth_first_search(self.tree, 'a')

# runs the unit tests
if __name__ == '__main__':
    unittest.main()
