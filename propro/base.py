"""Declares the interface to be implemented by protein data source"""

class Source:
    """Base class for protein data sources"""

    # Abstract methods to be overridden by subclasses

    def all_foods(self):
        """(Source) -> list of Food

        Return the names of all foods for which data are available from this
        source.
        """
        raise NotImplementedError(self.__class__.__name__)

    # Utility methods

    def foods_by_protein_content(self, protein_content):
        """(Source, float) -> list of Food

        Return a list of foods having at least the specified `protein_content`
        (i.e., fraction of calories from protein). The content should be a
        `float` between 0.0 (meaning "no protein") and 1.0 (meaning "all
        calories come from protein"), inclusive.
        """
        return [food for food in self.all_foods()
                if food.protein_content() >= protein_content]
