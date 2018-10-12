def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


import unittest


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 15), 25)
        self.assertEqual(add(-10, 10), 0)
        self.assertEqual(add(-1, -4), -5)
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 15), -5)
        self.assertEqual(subtract(-10, 10), -20)
        self.assertEqual(subtract(-1, -4), 3)
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(-1, -4), 4)
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(12, 4), 3)
        self.assertEqual(divide(10, 10), 1)
        self.assertEqual(divide(4, 1), 4)
        self.assertEqual(divide(10, 5), 2)

        self.assertRaises(ValueError, divide, 10, 0)