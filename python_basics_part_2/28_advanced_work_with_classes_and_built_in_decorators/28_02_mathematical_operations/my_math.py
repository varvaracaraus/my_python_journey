import math

from basic_math import BasicMath


class MyMath(BasicMath):
    """
    MyMath class provides class methods for various mathematical calculations.
    """

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Calculates the circumference of a circle given its radius.
        :param radius: radius of the circle
        :return: circumference of the circle
        """
        return 2 * cls().pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
        Calculates the area of a circle given its radius.
        :param radius: radius of the circle
        :return: area of the circle
        """
        return cls().pi * radius ** 2

    @classmethod
    def cube_volume(cls, side: float) -> float:
        """
        Calculates the volume of a cube given the length of its side.
        :param side: length of the cube's side
        :return: volume of the cube
        """
        return side ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        """
        Calculates the surface area of a sphere given its radius.
        :param radius: radius of the sphere
        :return: surface area of the sphere
        """
        return 4 * cls().pi * radius ** 2

    @classmethod
    def rectangle_area(cls, length: float, width: float) -> float:
        """
        Calculates the area of a rectangle.
        :param length: length of the rectangle
        :param width: width of the rectangle
        :return: area of the rectangle
        """
        return length * width

    @classmethod
    def rectangle_perimeter(cls, length: float, width: float) -> float:
        """
        Calculates the perimeter of a rectangle.
        :param length: length of the rectangle
        :param width: width of the rectangle
        :return: perimeter of the rectangle
        """
        return 2 * (length + width)

    @classmethod
    def triangle_area(cls, a: float, b: float, c: float) -> float:
        """
        Calculates the area of a triangle using Heron's formula.
        :param a: length of the first side
        :param b: length of the second side
        :param c: length of the third side
        :return: area of the triangle
        """
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @classmethod
    def sphere_volume(cls, radius: float) -> float:
        """
        Calculates the volume of a sphere.
        :param radius: radius of the sphere
        :return: volume of the sphere
        """
        return (4 / 3) * cls().pi * radius ** 3
