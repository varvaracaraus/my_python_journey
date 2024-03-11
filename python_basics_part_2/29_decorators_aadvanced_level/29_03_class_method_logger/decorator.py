import datetime
import functools
import time
from typing import Callable, Any


def log_methods(time_fmt: str) -> Callable:
    """ A decorator for logging class methods. """

    def class_decorator(cls: Any) -> Any:
        """ A class decorator applied to each method for logging. """
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                setattr(cls, attr_name, log_method(attr_value, time_fmt))
        return cls

    def log_method(method: Callable, fmt: str) -> Callable:
        """ A method decorator that adds logging before and after method execution. """

        @functools.wraps(method)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.time()
            print(f"Starting '{method.__qualname__}'. Start date and time: {datetime.datetime.now().strftime(fmt)}.")
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Finishing '{method.__qualname__}', execution time = {end_time - start_time:.3f} s.")
            return result

        return wrapper

    return class_decorator
