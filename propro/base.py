"""Declares the interface to be implemented by protein data source"""

class Source:
    """Base class for protein data sources"""

    # Abstract methods to be overridden by subclasses

    def all_foods(self):
        """(Source) -> list of str

        Return the names of all foods for which data are available from this
        source.
        """
        raise NotImplementedError(self.__class__.__name__)

    def calories_per_oz(self, food):
        """(Source, str) -> float

        Return the number of calories in one ounce of `food`; e.g. 30 calories
        in 1 oz of chicken breast.
        """
        raise NotImplementedError(self.__class__.__name__)

    def oz_per_serving(self, food):
        """(Source, str) -> float

        Return the number of ounces (by weight) of `food` per serving.
        """
        raise NotImplementedError(self.__class__.__name__)

    def protein_grams_per_oz(self, food):
        """(Source, str) -> float

        Return the number of grams of protein in in one ounce of `food`; e.g.
        1.0 gram of protein in one ounce of chicken breast.
        """
        raise NotImplementedError(self.__class__.__name__)

    # Utility methods

    def calories_per_serving(self, food):
        """(str) -> float

        Return the number of calories in one serving of `food`; e.g., 30
        calories in one serving (i.e., 1 oz) of chicken breast.
        """
        return self.calories_per_oz(food) * self.oz_per_serving(food)

    def foods_by_protein_content(self, protein_content):
        """(Source, float) -> list of str

        Return a list of foods having at least the specified `protein_content`
        (i.e., fraction of calories from protein). The content should be a
        `float` between 0.0 (meaning "no protein") and 1.0 (meaning "all
        calories come from protein"), inclusive.
        """
        return [food for food in self.all_foods()
                if self.protein_content(food) >= protein_content]

    def protein_content(self, food):
        cal = self.calories_per_oz(food)
        return self.protein_grams_per_oz(food) * 4 / cal if cal else 0
