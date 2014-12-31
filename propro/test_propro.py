"""Test driver for the entire proPro package."""

import sys
import unittest

sys.path.append('..')
import propro

class TestProPro(unittest.TestCase):

    def test_find_foods_by_protein_content(self):
        r = propro.find_foods_by_protein_content(0.5)
        self.assertEqual(list, type(r))

if __name__ == '__main__':
    unittest.main()
