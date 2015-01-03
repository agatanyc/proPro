"""Test driver for the entire proPro package."""

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), os.pardir))

from propro import mock

class TestSource(unittest.TestCase):

    def setUp(self):
        self.source = mock.Source()

    def test_foods_by_protein_content(self):
        r = self.source.foods_by_protein_content(0.5)
        self.assertEqual(list, type(r))

if __name__ == '__main__':
    unittest.main()
