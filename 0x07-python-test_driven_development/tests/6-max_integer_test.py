#!/usr/bin/python3
"""
   Unittest for max_integer

"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
        TestMaxInteger class
    """

    def test_positive(self):
        """
            checks for the highest positive integer
        """
        self.assertEqual(max_integer([3, 5, 1, 7]), 7)

    def test_negative(self):
        """
            Checks for highest negative integer
        """
        self.assertEqual(max_integer([-3, -7, -1, -5]), -1)

     def test_positive_float(self):
        """
            checks for the highest positive float
        """
        self.assertEqual(max_integer([2.95, 8.25, 3.25, 9.5]), 9.5)

    def test_neg_float(self):
        """
            checks for the highest negative float
        """
        self.assertEqual(max_integer([-2.95, -8.25, -3.25, -9.5]), -2.95)

    def test_char(self):
        """
            checks for the highest string
        """
        self.assertEqual(max_integer(['a', 'A', 'b', 'B']), 'b')

    def test_strings(self):
        """
            Checks if function can give the highest string
        """
        self.assertEqual(max_integer(['ama', 'Ama', 'bed', 'Bad']), 'bed')
        self.assertEqual(max_integer('Brains'), 'n')

    def test_if_all_negative_integers(self):
        """Checks if all arguments are negative"""

        self.assertEqual(max_integer([-3, -7, -6, -8]), -3)

    def test_if_list_empty(self):
        """checks for if list is empty"""

        self.assertIsNone(max_integer([]))

    def test_if_no_arguments(self):
        """checks for if no args is provided"""

        self.assertIsNone(max_integer())

    def test_if_none_is_arg(self):
        """checks for if none is provided"""

        self.assertRaises(TypeError, max_integer, None)

    def test_if_a_wrong_type_in_list(self):
        """checks for if a wrong type is provided"""

        self.assertRaises(TypeError, max_integer, [4, 3, "key", -5])

    def test_if_float_is_in_list(self):
        """checks for if float is provided"""

        self.assertEqual(max_integer([-2.4, 3.7, 4.5, 1.5]), 4.5)


if __name__ == "__main__":
    unittest.main()
