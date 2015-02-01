"""Provides a source of nutrition data from the U.S. Dept. of Agriculture."""

from . import base
from . import food

import json
import os

_OZ_PER_100G = 3.5274       # The USDA reports values per 100 grams.

def _get_nutrient_value_per_100g(data, key):
    return next(float(nutrient['value']) / _OZ_PER_100G
                for nutrient in data['nutrients']
                if nutrient['abbr'] == key)

def _loadf(fname):
    """(str) -> object

    Return the USDA data contents of the JSON file at path `fname`.
    """
    with open(fname, encoding="ISO-8859-1") as f:
        return json.load(f)

def get_names(data):
    block = data['name']
    names = block['common'] + [block['long']] + [block['sci']]
    return [name for name in names if name]

def get_calories_per_oz(data):
    return _get_nutrient_value_per_100g(data, "ENERC_KCAL")

def get_oz_per_serving(data):
    pass # TODO

def get_protein_grams_per_oz(data):
    return _get_nutrient_value_per_100g(data, "PROCNT")

def make_food(data):            # data is a result of calling _loadf(fname)
    return food.Food(
            get_names(data),
            get_calories_per_oz(data),
            get_oz_per_serving(data),
            get_protein_grams_per_oz(data))

class USDASource(base.Source):
    """Protein data source returning information from the USDA."""

    # This class loads data from JSON files as needed.

    # Overrides of base Source

    def __init__(self, path):
        """`path` is a directory of JSON files of exported USDA data."""
        self._path = path

    def all_foods(self):
        fnames = [os.path.join(self._path, name)
                    for name in os.listdir(self._path)
                    if not name.startswith('.')]
        return [make_food(_loadf(fname)) for fname in fnames]
