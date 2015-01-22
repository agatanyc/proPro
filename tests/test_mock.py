"""Test driver for propro.mock"""

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), os.pardir))

from propro import mock

class TestMockSource(unittest.TestCase):

    def setUp(self):
        self.foods = mock.Source().all_foods()

    def test_all_foods_returns_list(self):
        self.assertEqual(list, type(self.foods))

    def test_all_foods_returns_non_empty(self):
        self.assertTrue(self.foods)

    def test_all_foods_returns_unique_values(self):
        self.assertEqual(len(self.foods), len(set(self.foods)))

    def test_calories_per_oz(self):
        for food in self.foods:
            self.assertGreaterEqual(food.calories_per_oz(), 0)

    def test_oz_per_serving(self):
        for food in self.foods:
            self.assertGreaterEqual(food.oz_per_serving(), 0)

    def test_protein_grams_per_oz(self):
        for food in self.foods:
            self.assertGreaterEqual(food.protein_grams_per_oz(), 0)

if __name__ == '__main__':
    unittest.main()
