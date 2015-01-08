"""Declares the interface to be implemented by Protein data source"""

class Source:
    """Base class for Protein data sources"""

    # Utility methods

    def calories_per_serving(self, food):
        """(str) -> float

        Return the number of calories in one serving of `food`; e.g., 30
        calories in one serving (i.e., 1 oz) of chicken breast.
        """
        return self.calories_per_oz() * self.oz_per_serving()

    # Abstract methods to be overridden by subclasses

    def foods_by_protein_content(self, protein_content):
        """(float) -> list of str

        Return a list of foods having at least the specified `protein_content`
        (i.e., fraction of calories from protein). The content should be a
        `float` between 0.0 (meaning "no protein") and 1.0 (meaning "all
        calories come from protein"), inclusive.
        """
        raise NotImplementedError(self.__class__.__name__)

    def protein_grams_per_oz(self, food):
        """(str) -> float

        Return the number of grams of protein in in one ounce of `food`; e.g.
        1.0 gram of protein in one ounce of chicken breast.
        """
        raise NotImplementedError(self.__class__.__name__)

    def oz_per_serving(self, food):
        """(str) -> float

        Return the number of ounces (by weight) of `food` per serving.
        """
        raise NotImplementedError(self.__class__.__name__)

    def calories_per_oz(self, food):
        """(str) -> float

        Return the number of calories in one ounce of `food`; e.g. 30 calories
        in 1 oz of chicken breast.
        """
        raise NotImplementedError(self.__class__.__name__)
