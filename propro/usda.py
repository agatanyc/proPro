"""Provides a source of nutrition data from the U.S. Dept. of Agriculture."""

from . import base

import json
import os

def _loadf(fname):
    """(str) -> object"""
    with open(fname, encoding="ISO-8859-1") as f:
        return json.load(f)

def get_name(data):
    return data['name']['long']

class Source(base.Source):
    """Protein data source returning information from the USDA."""

    # This class loads data from JSON files as needed.

    # Overrides of base Source

    def __init__(self, path):
        """`path` is a directory of JSON files of exported USDA data."""
        self._path = path

    def all_foods(self):
        return [get_name(_loadf(os.path.join(self._path, f)))
                for f in os.listdir(self._path)]

    def calories_per_oz(self, food):
        pass # TODO

    def oz_per_serving(self, food):
        pass # TODO

    def protein_grams_per_oz(self, food):
        pass # TODO
