class Property:
    """
    Base class representing a property with a specific value.
    """

    def __init__(self, worth: float):
        """
        Initialize the property with its worth.

        Args:
            worth (float): The worth of the property.
        """
        self._worth = worth

    def tax(self) -> float:
        """
        Calculate the tax for the property. Must be implemented in subclasses.

        Raises:
            NotImplementedError: If not implemented in subclasses.
        """
        raise NotImplementedError("Must be implemented in subclasses")

    def get_worth(self) -> float:
        """
        Get the worth of the property.

        Returns:
            float: The worth of the property.
        """
        return self._worth

    def set_worth(self, value: float) -> None:
        """
        Set the worth of the property.

        Args:
            value (float): The new worth of the property.
        """
        self._worth = value
