import math


class BasicMath:
    """
    Base class providing basic mathematical operations.
    """

    def __init__(self):
        self._pi = math.pi

    @property
    def pi(self) -> float:
        """
        Returns the value of π.
        """
        return self._pi

    @pi.setter
    def pi(self, value: float):
        """
        Sets the value of π.
        """
        self._pi = value
