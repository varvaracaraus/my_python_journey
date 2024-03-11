from typing import Callable


def check_permission(permission: str) -> Callable:
    """
    A decorator to check if the user has the required permission.

    Args:
        permission (str): The required permission to execute the function.

    Returns:
        Callable: The decorated function.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"user does not have enough rights to execute the function {func.__name__}")

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site() -> None:
    """Deletes the site."""
    print('Deleting site')


@check_permission('user_1')
def add_comment() -> None:
    """Adds a comment."""
    print('Adding comment')


delete_site()
try:
    add_comment()
except PermissionError as error:
    print(f"PermissionError: {error}")
