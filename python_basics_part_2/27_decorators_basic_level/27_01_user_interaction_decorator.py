import functools


def user_interaction_decorator(func):
    """
    A decorator that adds user interaction before the execution of the function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapper function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input("How are you? ")
        print("I'm not so great! Okay, here's your function.")
        return func(*args, **kwargs)

    return wrapper


@user_interaction_decorator
def demonstrate_decorator():
    """
    A demonstration function to show the decorator's effect.
    """
    print("<Something is happening here...>")


# Run the demonstration
demonstrate_decorator()
