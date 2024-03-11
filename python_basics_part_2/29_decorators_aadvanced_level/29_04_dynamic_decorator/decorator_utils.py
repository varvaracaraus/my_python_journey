from typing import Callable


def decorator_with_args_for_another_decorator(decorator: Callable) -> Callable:
    """
    A decorator for decorators, allowing them to accept arbitrary arguments.
    """

    def wrapper(*args, **kwargs) -> Callable:
        def inner_decorator(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return inner_decorator

    return wrapper
