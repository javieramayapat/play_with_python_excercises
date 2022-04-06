import unittest
from unit_test_example.circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    # test the happy paths
    def test_area(self):
        # Test area when radious >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    # test if my function handles improper inputs correctly and raises a value error
    def test_values(self):
        # Make sure value error are raised when necessary
        # We use assert raise method (exception class, functions, arguments to the function)
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
