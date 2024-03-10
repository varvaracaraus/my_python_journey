import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    This class defines a common interface for calculating the area of a shape.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Abstract method to calculate the area of the shape. Must be overridden in each subclass.

        Returns:
            float: The area of the shape.
        """
        pass


class Circle(Shape):
    """ Represents a circle."""

    def __init__(self, radius: float) -> None:
        self.__radius = radius

    @property
    def radius(self) -> float:
        """Returns the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Sets the radius of the circle."""
        self.__radius = value

    def area(self) -> float:
        """Calculates and returns the area of the circle."""
        return math.pi * self.__radius ** 2


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self) -> float:
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self) -> float:
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        """Sets the height of the rectangle."""
        self.__height = value

    def area(self) -> float:
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height


class Triangle(Shape):
    """Represents a triangle."""

    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height

    @property
    def base(self) -> float:
        """Returns the base of the triangle."""
        return self.__base

    @base.setter
    def base(self, value: float) -> None:
        """Sets the base of the triangle."""
        self.__base = value

    @property
    def height(self) -> float:
        """Returns the height of the triangle."""
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        """Sets the height of the triangle."""
        self.__height = value

    def area(self) -> float:
        """Calculates and returns the area of the triangle."""
        return 0.5 * self.__base * self.__height
