from singleton_decorator import singleton


@singleton
class Example:
    """
    An example class to demonstrate the singleton pattern.
    """
    pass


# Creating instances of the Example class
my_obj = Example()
my_another_obj = Example()

# Printing the object IDs
print(id(my_obj))
print(id(my_another_obj))

# Checking if both variables refer to the same object
print(my_obj is my_another_obj)
