"""Test driver for propro.mock"""

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), os.pardir))

from propro import mock

class TestMockSource(unittest.TestCase):

    def setUp(self):
        self.source = mock.Source()
        self.chicken = 'Chicken'

    def test_all_foods_returns_list(self):
        foods = self.source.all_foods()
        self.assertEqual(list, type(foods))

    def test_all_foods_returns_non_empty(self):
        foods = self.source.all_foods()
        self.assertTrue(foods)

    def test_all_foods_returns_unique_values(self):
        foods = self.source.all_foods()
        self.assertEqual(len(foods), len(set(foods)))

    def test_calories_per_oz(self):
        cal = self.source.calories_per_oz(self.chicken)
        self.assertGreaterEqual(cal, 0)

    def test_oz_per_serving(self):
        self.assertGreater(self.source.oz_per_serving(self.chicken), 0)

    def test_protein_grams_per_oz(self):
        g = self.source.protein_grams_per_oz(self.chicken)
        self.assertGreaterEqual(g, 0)

if __name__ == '__main__':
    unittest.main()
