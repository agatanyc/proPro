"""Test driver for propro.base"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(
    os.path.dirname(sys.argv[0]),
    os.pardir,
    'propro'))

import food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.chicken = food.Food('chicken', 10, 6, 2)

    # TODO Test assigned properties

    # Test utility methods

    def test_calories_per_serving(self):
        actual = self.chicken.calories_per_serving()
        self.assertEqual(60, actual)

    def test_protein_content(self):
        self.assertEqual(0.8, self.chicken.protein_content())

if __name__ == '__main__':
    unittest.main()
