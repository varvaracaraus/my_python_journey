# Custom Zip Generator
# This script creates a generator for pairs of elements from two input iterables - a string and a tuple of numbers.

def custom_zip(iterable1, iterable2):
    """
    Creates a generator that yields tuples of elements from two given iterables.

    Args:
        iterable1: The first iterable.
        iterable2: The second iterable.

    Returns:
        A generator that yields pairs (tuples) of elements from the given iterables.
    """
    return ((item1, item2) for item1, item2 in zip(iterable1, iterable2))


def run_program():
    """
    Runs the main program to take user inputs and generate paired elements using a custom zip generator.
    """
    string_data = input("Enter a string: ")
    tuple_numbers = tuple(map(int, input("Enter numbers (separated by space): ").split()))

    # Using the custom zip generator
    pairs_generator = custom_zip(string_data, tuple_numbers)

    print("\nPairs generated:")
    for pair in pairs_generator:
        print(pair)


# Running the main function
run_program()
