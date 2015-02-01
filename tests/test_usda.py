"""Test driver for propro.usda"""

import os
import sys
import unittest

here = os.path.dirname(__file__)  # the folder where this script lives
sys.path.append(os.path.join(here, os.pardir))

from propro import usda

class TestUSDASource(unittest.TestCase):

    def setUp(self):
        self.source = usda.USDASource(os.path.join(here, "data"))
        self.foods = self.source.all_foods()

    def test_all_foods_returns_list(self):
        self.assertEqual(list, type(self.foods))

    def test_all_foods_returns_non_empty(self):
        self.assertTrue(self.foods)

    def test_all_foods_returns_unique_values(self):
        self.assertEqual(len(self.foods), len(set(self.foods)))

    def test_all_foods_have_names(self):
        self.assertTrue(all(food.names() for food in self.foods))

    def test_all_foods_have_nonnegative_calories_per_oz(self):
        self.assertTrue(all(f.calories_per_oz() >= 0 for f in self.foods))

#   def test_oz_per_serving(self):
#       self.assertGreater(self.source.oz_per_serving(self.chicken), 0)

#   def test_protein_grams_per_oz(self):
#       g = self.source.protein_grams_per_oz(self.chicken)
#       self.assertGreaterEqual(g, 0)

if __name__ == '__main__':
    unittest.main()
