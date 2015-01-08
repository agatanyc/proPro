"""Protein data source wrapper"""

__version__ = '0.1.0'

from . import mock

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
    return usda.Source()    # TODO
