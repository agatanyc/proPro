"""Provides a source of nutrition data from the U.S. Dept. of Agriculture."""

from . import base

import json
import os

def _loadf(fname):
    """(str) -> object"""       # returns json file with USDA data
    with open(fname, encoding="ISO-8859-1") as f:
        return json.load(f)

def get_name(data):             # returns `long name` of food item
    return data['name']['long']

def get_calories(data):
    pass # TODO

def get_oz_per_serving(data):
    pass # TODO

def get_protein_grams_per_oz(data):
    pass # TODO

class Source(base.Source):
    """Protein data source returning information from the USDA."""

    # This class loads data from JSON files as needed.

    # Overrides of base Source

    def __init__(self, path):
        """`path` is a directory of JSON files of exported USDA data."""
        self._path = path

    def all_foods(self):          # returns list of `long names`
        return [get_name(_loadf(os.path.join(self._path, f)))
                for f in os.listdir(self._path)]

    #def calories_per_oz(self, food):

    #def oz_per_serving(self):

    #def protein_grams_per_oz(self):
