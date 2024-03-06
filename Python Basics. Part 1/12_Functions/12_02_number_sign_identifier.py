# Number Sign Identifier
# This script defines a main function 'test' that determines if a user-input number is positive or negative.
# Based on the input, it calls one of two functions: 'positive' for positive numbers, and
# 'negative' for negative numbers.

def test() -> None:
    """
    Receives a number from the user, then calls either 'positive' or 'negative' based on the sign of the number.
    """
    number = int(input('Enter the number: '))
    if number > 0:
        positive()
    else:
        negative()


def positive() -> None:
    """
    Prints that the number is positive.
    """
    print('Positive')


def negative() -> None:
    """
    Prints that the number is negative.
    """
    print('Negative')


# Call the main function
test()
