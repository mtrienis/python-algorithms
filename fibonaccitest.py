from fibonacci import Fibonacci

import unittest

# test class for the triangle class
class TestFibonacci(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.fibonacci = Fibonacci()

    def test_fib(self):
        result = self.fibonacci.fib(9)
        self.assertEqual(result, 34)

    def test_fib_recursive(self):
        result = self.fibonacci.fib_recursive(9)
        self.assertEqual(result, 34)


# runs the unit tests
if __name__ == '__main__':
    unittest.main()