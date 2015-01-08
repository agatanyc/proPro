"""Test driver for propro.base"""

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), os.pardir))

from propro import base

class TestBaseSourceAbstractMethods(unittest.TestCase):

    def setUp(self):
        self.source = base.Source()
        self.arbitraryContent = 0.5
        self.arbitraryFood = 'chicken'

    def test_foods_by_protein_content(self):
        self.assertRaises(
                NotImplementedError,
                self.source.foods_by_protein_content,
                self.arbitraryContent)

    def test_protein_grams_per_oz(self):
        self.assertRaises(
                NotImplementedError,
                self.source.protein_grams_per_oz,
                self.arbitraryFood)

    def test_oz_per_serving(self):
        self.assertRaises(
                NotImplementedError,
                self.source.oz_per_serving,
                self.arbitraryFood)

    def test_calories_per_oz(self):
        self.assertRaises(
                NotImplementedError,
                self.source.calories_per_oz,
                self.arbitraryFood)

class TestBaseSourceUtilityMethods(unittest.TestCase):

    def setUp(self):
        self.arbitraryFood = 'chicken'

    class DummySource(base.Source):

        def calories_per_oz(self, food):
            return 6

        def oz_per_serving(self, food):
            return 9

    def test_calories_per_serving(self):
        source = TestBaseSourceUtilityMethods.DummySource()
        self.assertEqual(54, source.calories_per_serving(self.arbitraryFood))

if __name__ == '__main__':
    unittest.main()

