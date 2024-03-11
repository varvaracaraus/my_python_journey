import functools
import time
from typing import Callable


def delay_execution(seconds: int) -> Callable:
    """
    A decorator that delays the execution of a function by a given number of seconds.

    Args:
        seconds (int): The number of seconds to delay the function execution.

    Returns:
        Callable: The decorated function with added delay.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting for {seconds} seconds before executing '{func.__name__}'...")
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@delay_execution(4)
def demonstrate_delay():
    """
    A demonstration function to show the effect of the delay_execution decorator.
    """
    print("Function is now executing.")


# Run the demonstration function
demonstrate_delay()
