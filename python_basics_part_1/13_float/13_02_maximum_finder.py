# Maximum Finder
# This script defines functions to find the maximum of two numbers and the maximum of three numbers.
# It takes three numbers as input from the user and then uses these functions to find the maximum.

def maximum_of_two(num1: int, num2: int) -> int:
    """
    Returns the maximum of two given numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The maximum of num1 and num2.
    """
    return num1 if num1 > num2 else num2


def maximum_of_three(num1: int, num2: int, num3: int) -> int:
    """
    Returns the maximum of three given numbers.

    :param num1: The first number.
    :param num2: The second number.
    :param num3: The third number.
    :return: The maximum of num1, num2, and num3.
    """
    return maximum_of_two(maximum_of_two(num1, num2), num3)


# Get user input
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

# Calculate the maximum and print the result
result = maximum_of_three(first_number, second_number, third_number)
print('Maximum of three numbers:', result)
