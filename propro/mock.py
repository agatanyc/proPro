"""Provides a source of dummy data"""

from . import base

PROTEIN_GRAMS_PER_OZ, OZ_PER_SERVING, CALORIES_PER_OZ = range(3)

_data = { 'Chicken':          (     6, 6, 30),
          'Cottage Cheese':   (     3, 4, 20),
          'Greek Yogurt':     (  2.75, 8, 16),
          'Candy':            (     0, 1, 60) }

class Source(base.Source):
    """Protein data source returning only dummy data"""

    # Overrides of base Source

    def all_foods(self):
        return list(_data.keys())

    def calories_per_oz(self, food):
        return _data[food][CALORIES_PER_OZ]

    def oz_per_serving(self, food):
        return _data[food][OZ_PER_SERVING]

    def protein_grams_per_oz(self, food):
        return _data[food][PROTEIN_GRAMS_PER_OZ]
