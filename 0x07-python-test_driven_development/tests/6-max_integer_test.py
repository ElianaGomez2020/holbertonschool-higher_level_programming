#!/usr/bin/python3
"""

Unitests for max_integer 
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]   
    """

    def test_number_list(self)
        """Number list cases"""
        self.assertEqual(max_integer([1, 50, 2]), 50)
        self.assertEqual(max_integer([-5, -10, -9]), -5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 4] * 3), 4)

    def test_empty(self)
        """Empty lists """
        self.assertEqual(max_integer([]), None)

    def test_not_list(self)
        """Not number list"""
        self.assertEqual(max_integer(['a', 'b', 'c']), a)
        self.assertEqual(max_integer(('a', 'b', 'c')), a)
