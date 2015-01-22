"""Protein data source wrapper"""

__version__ = '0.1.0'

from . import mock
from . import usda

import os

# Factory methods

def mock_source():
    """() -> Source

    Return a source of dummy data.
    """
    return mock.Source()

def usda_source():
    """() -> Source

    Return a source of data from the USDA.
    """
    here = os.path.dirname(os.path.realpath(__file__)) # propro
    path = os.path.join(here, 'nice') 
    """`path` is a directory of JSON files of exported USDA data."""

    return usda.Source(path)
