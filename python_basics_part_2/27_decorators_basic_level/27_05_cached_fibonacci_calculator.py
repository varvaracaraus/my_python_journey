import functools
from typing import Callable, Dict


def caching_decorator(func: Callable) -> Callable:
    """
    A decorator that caches the results of function calls.

    This decorator stores the results of previous calls to the decorated function in a cache,
    and returns the cached result for repeated calls with the same arguments.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with caching capability.
    """
    cache_dict: Dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper


@caching_decorator
def fibonacci(number: int) -> int:
    """
    Calculates the Fibonacci number for the given input using recursion.

    Args:
        number (int): The Fibonacci sequence position to calculate.

    Returns:
        int: The Fibonacci number at the specified position.
    """
    if number <= 1:
        return number
    print(f"Calculating fibonacci({number})")
    return fibonacci(number - 1) + fibonacci(number - 2)


# Demonstrate the use of cached Fibonacci calculation
print(fibonacci(10))  # The result will be calculated and cached
print(fibonacci(10))  # The result will be retrieved from the cache
print(fibonacci(5))  # The result will be retrieved from the cache
print(fibonacci(18))  # The result will be calculated and cached
