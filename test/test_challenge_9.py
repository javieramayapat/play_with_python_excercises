import unittest
from list_tuples.challenge_9 import count_amount_of_vowels_in_text


class TestChallenge9(unittest.TestCase):
    def test_count_amount_of_vowels_in_text_with_a_string(self):
        # first step: prepare test's data
        string = "ana"
        d1 = {"a": 2, "e": 0, "i": 0, "o": 0, "u": 0}

        # second step: execute the function that you want to test
        d2 = count_amount_of_vowels_in_text(string)

        # comprobar que el test hace lo que tiene que hacer (asserts)
        self.assertDictEqual(d1, d2)

    def test_count_amount_of_vowels_in_text_with_an_empty_string(self):
        self.assertRaises(ValueError, count_amount_of_vowels_in_text, "")

    def test_count_amount_of_vowels_in_text_with_invalid_inputs(self):
        # self.assertRaises()
        pass
