from typing import Callable

from decorator_utils import decorator_with_args_for_another_decorator


@decorator_with_args_for_another_decorator
def decorated_decorator(func: Callable, *decorator_args, **decorator_kwargs) -> Callable:
    """
    A decorator that prints the arguments passed to it, and then calls the original function.
    """

    def wrapper(*func_args, **func_kwargs) -> None:
        print("Arguments and keyword arguments passed to the decorator:", decorator_args, decorator_kwargs)
        return func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(100, 'dollars', 200, 'friends')
def decorated_function(text: str, num: int) -> None:
    """
    A function that will be decorated. Prints a greeting with the passed parameters.
    """
    print("Hello", text, num)


# Testing the decorated function
decorated_function("User", 101)
