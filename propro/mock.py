"""Protein data source returning only dummy data"""

class Source:

    def foods_by_protein_content(self, protein_content):
        """(float) -> list of str

        Return a list of foods having at least the specified `protein_content`
        (i.e., fraction of calories from protein). The content should be a
        `float` between 0.0 (meaning "no protein") and 1.0 (meaning "all
        calories come from protein"), inclusive.
        """
        return pass

    def protein_grams_per_oz(self, food):
        """(str) -> float

        Return the number of grams of protein in in one ounce of `food`; e.g.
        1.0 gram of protein in one ounce of chicken breast.
        """
        pass

    def serving_size(self, food):
        """(str) -> float

        Return the number of ounces (by weight) of `food` per serving.
        """
        pass

    def calories_per_oz(self, food):
        """(str) -> float

        Return the number of calories in one ounce of `food`; e.g. 30 calories
        in 1 oz of chicken breast.
        """
        pass
