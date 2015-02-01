"""Declares a class representing kinds of food (e.g., salted butter)."""

class Food:

    # TODO Document parameters.
    def __init__(
            self,
            names,
            calories_per_oz,
            oz_per_serving,
            protein_grams_per_oz):
        """(Food, list of str, float, float, float) -> NoneType"""
        self._names                = names[:]
        self._calories_per_oz      = calories_per_oz
        self._oz_per_serving       = oz_per_serving
        self._protein_grams_per_oz = protein_grams_per_oz

    def __repr__(self):
        return self.names()[0]

    def names(self):
        """(Food) -> list of str

        Return all known names (common, scientific, etc.) of this Food.
        """
        return self._names[:]   # Copy to prevent inadvertent modification.

    def calories_per_oz(self):
        """(Food) -> float

        Return the number of calories in one ounce of this food; e.g., 30
        calories in 1 oz of chicken breast.
        """
        return self._calories_per_oz

    def oz_per_serving(self):
        """(Food) -> float

        Return the number of ounces (by weight) of this Food per serving.
        """
        return self._oz_per_serving

    def protein_grams_per_oz(self):
        """(Food) -> float

        Return the number of grams of protein in in one ounce of this Food;
        e.g., 1.0 gram of protein in one ounce of chicken breast.
        """
        return self._protein_grams_per_oz

    # Utility methods

    def calories_per_serving(self):
        """(Food) -> float

        Return the number of calories in one serving of this Food; e.g., 30
        calories in one serving (i.e., 1 oz) of chicken breast.
        """
        return self.calories_per_oz() * self.oz_per_serving()

    def protein_content(self):
        """(Food) -> float

        Return the percentage of calories in this Food coming from protein.
        """
        cal = self.calories_per_oz()
        return self.protein_grams_per_oz() * 4 / cal if cal else 0
