import unittest

from Fibo import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci(1)) 
    def test_1(self):
        self.assertEqual(2, fibonacci(2)) 
    def test_1(self):
        self.assertEqual(3, fibonacci(3)) 
    def test_1(self):
        self.assertEqual(5, fibonacci(5)) 