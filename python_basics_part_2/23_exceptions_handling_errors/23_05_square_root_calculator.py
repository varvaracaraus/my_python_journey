# Square Root Calculator
# This script calculates the square root of a given number, handling possible errors gracefully.

import math


def calculate_square_root(number) -> float | str:
    """
    Calculates the square root of a number, with error handling for invalid input.

    Args:
        number (int or float): The number for which to calculate the square root.

    Returns:
        float or str: The square root of the number if valid, otherwise an error message.
    """
    try:
        if not isinstance(number, (int, float)):
            raise TypeError("Input value must be a number")
        if number < 0:
            raise ValueError("Negative numbers cannot have a square root")

        result = math.sqrt(number)
        return result
    except ValueError as ve:
        return f"Error: {ve}"
    except TypeError as te:
        return f"Error: {te}"
    except Exception as e:
        return f"Unexpected error: {e}"


# Test cases for the square root calculator
numbers = [16, 25, -9, 0, 4.5, "abc"]
for numb in numbers:
    res = calculate_square_root(numb)
    print(f"Square root of number {numb}: {res}")
