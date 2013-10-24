from quicksort import QuickSort

import unittest

# test class for the triangle class
class TestQuickSort(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.items = [38, 27, 43, 50, 9, 82, 10]
        self.sort = QuickSort()

        
    def test_quick_sort(self):
        print '---- quicksort ----'
        print self.sort.quick_sort(self.items, 0, 6)


# runs the unit tests
if __name__ == '__main__':
    unittest.main()
