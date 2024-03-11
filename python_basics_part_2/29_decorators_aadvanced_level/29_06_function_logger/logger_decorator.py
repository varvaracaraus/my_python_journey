import time
from functools import wraps
from typing import Callable, Any


class LoggerDecorator:
    """
    A decorator for logging the arguments, result, and execution time of a function.

    Attributes:
        func (Callable): The function to be decorated.
    """

    def __init__(self, func: Callable):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Called when the decorated function is invoked.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the decorated function's execution.
        """
        start_time = time.time()
        print(f"Calling function {self.func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Result: {result}")
        print(f"Execution time: {end_time - start_time} seconds")
        return result
