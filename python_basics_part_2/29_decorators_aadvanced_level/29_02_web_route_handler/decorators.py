from typing import Callable, Dict, Optional

routes: Dict[str, Callable] = {}


def log_call(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def callback(route: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        routes[route] = func
        return func

    return decorator


def get_route(route: str) -> Optional[Callable]:
    return routes.get(route)
