import datetime
import functools
from typing import Callable, Any


def logging_decorator(func: Callable) -> Callable:
    """
    A decorator for logging function details and errors.

    Logs the name and documentation of the function to the console. If an error occurs during the function's execution,
    it logs the function name and the error to 'function_errors.log', along with the date and time of the error.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print(f"Function '{func.__name__}' is called.")
            print(f"Documentation: {func.__doc__}")
            return func(*args, **kwargs)
        except Exception as e:
            with open("function_errors.log", "a") as log_file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - Error in '{func.__name__}': {e}\n")
            print(f"An error occurred in '{func.__name__}'. Check 'function_errors.log' for details.")
            return None

    return wrapper


@logging_decorator
def demonstrate_logging():
    """
    A demonstration function to show the effect of the logging_decorator.
    This function intentionally raises an error.
    """
    raise ValueError("An intentional error for testing purposes.")


# Run the demonstration function
demonstrate_logging()
