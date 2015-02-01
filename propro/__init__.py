"""Provides access to protein data sources"""

__version__ = '0.1.0'

from . import mock
from . import usda

import os

# Factory methods

def mock_source():
    """() -> Source

    Return a source of dummy data.
    """
    return mock.MockSource()

def usda_source(path=None):
    """() -> Source

    Return a source of data from the USDA.  The `path` is a directory of JSON
    files of exported USDA data, and defaults to a directory of USDA SR25 data.
    """
    if not path:
        here = os.path.dirname(os.path.realpath(__file__)) # propro
        path = os.path.join(here, 'data')

    return usda.USDASource(path)
