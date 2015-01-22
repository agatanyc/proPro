"""Test driver for propro.base"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(
    os.path.dirname(sys.argv[0]),
    os.pardir,
    'propro'))

import base
import food

class TestBaseSource(unittest.TestCase):

    class DummySource(base.Source):
        def all_foods(self):
            return [food.Food(['chicken'],      10, 6, 2),
                    food.Food(['greek yogurt'], 10, 6, 1)]

    def test_all_foods(self):
        source = base.Source()
        self.assertRaises(NotImplementedError, source.all_foods)

    def test_foods_by_protein_content(self):
        source = TestBaseSource.DummySource()
        result = source.foods_by_protein_content(0.5)
        self.assertEqual(1, len(result))
        self.assertTrue('chicken' in result[0].names())

if __name__ == '__main__':
    unittest.main()
