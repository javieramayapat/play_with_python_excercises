import unittest
from list_tuples.challenge_8 import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    # check happy path
    def test_is_palindrome(self):
        # test palindrome when has a correct palindrome is in uppercase,
        self.assertAlmostEqual(is_palindrome("Ana"), True)
        self.assertAlmostEqual(is_palindrome("ojo"), True)
        # when has accents and spaces
        self.assertAlmostEqual(is_palindrome("Amó la paloma"), True)
        self.assertAlmostEqual(is_palindrome("Yo hago yoga hoy"), True)
        self.assertAlmostEqual(is_palindrome("Sé verlas al revés"), True)

    # test if my function handles improper inputs correctly and raises a value error
    def test_values(self):
        self.assertRaises(ValueError, is_palindrome, "")

    # Check if my function handle inproper inputs correctly and raises a value error
    def test_types(self):
        self.assertRaises(TypeError, is_palindrome, True)
        self.assertRaises(TypeError, is_palindrome, 15)
        self.assertRaises(TypeError, is_palindrome, 18.56)
        self.assertRaises(TypeError, is_palindrome, None)
