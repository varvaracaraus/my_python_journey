# Prime Index Cryptography
# This script filters elements of an iterable (like a list or a string) based on whether their indices are
# prime numbers.

def is_prime(num: int) -> bool:
    """
    Determines if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def crypto(iterable) -> list:
    """
    Filters elements of an iterable based on whether their indices are prime numbers.

    Args:
        iterable: An iterable (e.g., list or string).

    Returns:
        list: A list of elements whose indices are prime numbers.
    """
    return [element for index, element in enumerate(iterable) if is_prime(index)]


# Testing the function with a list and a string
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
