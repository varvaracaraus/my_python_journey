import functools
from typing import Callable, Any


def call_counter(func: Callable) -> Callable:
    """
    A decorator that counts and displays the number of times a decorated function is called.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with an added counter feature.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.count} times.")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@call_counter
def demonstrate_call_counter():
    """
    A demonstration function to show the effect of the call_counter decorator.
    """
    print("Function is executing.")


# Demonstrate the call counter functionality
demonstrate_call_counter()
demonstrate_call_counter()
demonstrate_call_counter()
demonstrate_call_counter()
