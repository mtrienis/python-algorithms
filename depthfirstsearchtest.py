from depthfirstsearch import DepthFirstSearch

import unittest

# test class for the triangle class
class TestDepthFirstSearch(unittest.TestCase):

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

        self.search = DepthFirstSearch()

        
    def test_depth_first_search(self):
        print '---- depth first search ----'
        print self.search.depth_first_search(self.tree, 'a')


# runs the unit tests
if __name__ == '__main__':
    unittest.main()
