"""Provides a source of dummy data"""

from . import base
from . import food

CALORIES_PER_OZ, OZ_PER_SERVING, PROTEIN_GRAMS_PER_OZ = range(3)

_data = { 'Chicken':          ( 30,  6,    6),
          'Cottage Cheese':   ( 20,  4,    3),
          'Greek Yogurt':     ( 16,  8, 2.75),
          'Candy':            ( 60,  1,    0) }

class Source(base.Source):
    """Protein data source returning only dummy data"""

    # Overrides of base Source

    def all_foods(self):
        return [food.Food([name], *value) for name, value in _data.items()]
