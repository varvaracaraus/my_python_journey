from typing import Callable, Type, TypeVar, Dict

T = TypeVar('T')


def singleton(cls: Type[T]) -> Callable:
    """
    A decorator that ensures a class has only one instance and provides a global point of access to it.
    """
    instances: Dict[Type[T], T] = {}

    def get_instance(*args, **kwargs) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
