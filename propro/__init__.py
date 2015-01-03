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

# Utility methods

def calories_per_serving(food):
    """(str) -> float

    Return the number of calories in one serving of `food`; e.g., 30
    calories in one serving (i.e., 1 oz) of chicken breast.
    """
    pass
