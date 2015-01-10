"""Test driver for propro.base"""

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), os.pardir))

from propro import base

class TestBaseSourceAbstractMethods(unittest.TestCase):

    def setUp(self):
        self.arbitraryContent = 0.5
        self.arbitraryFood = 'chicken'
        self.source = base.Source()

    def test_all_foods(self):
        self.assertRaises(
                NotImplementedError,
                self.source.all_foods)

    def test_calories_per_oz(self):
        self.assertRaises(
                NotImplementedError,
                self.source.calories_per_oz,
                self.arbitraryFood)

    def test_oz_per_serving(self):
        self.assertRaises(
                NotImplementedError,
                self.source.oz_per_serving,
                self.arbitraryFood)

    def test_protein_grams_per_oz(self):
        self.assertRaises(
                NotImplementedError,
                self.source.protein_grams_per_oz,
                self.arbitraryFood)

class TestBaseSourceUtilityMethods(unittest.TestCase):

    class DummySource(base.Source):

        def all_foods(self):
            return ['chicken', 'greek_yogurt']

        def calories_per_oz(self, food):
            return 10

        def oz_per_serving(self, food):
            return 6

        def protein_grams_per_oz(self, food):
            return 2 if food == 'chicken' else 1

    def setUp(self):
        self.source = TestBaseSourceUtilityMethods.DummySource()

    def test_calories_per_serving(self):
        actual = self.source.calories_per_serving('chicken')
        self.assertEqual(60, actual)

    def test_foods_by_protein_content(self):
        actual = self.source.foods_by_protein_content(0.5)
        self.assertEqual(['chicken'], actual)

    def test_protein_content(self):
        self.assertEqual(0.8, self.source.protein_content('chicken'))

if __name__ == '__main__':
    unittest.main()
