# Enhanced Digit Calculator
# This script performs various operations on the digits of a number based on user input.
# The operations include calculating the sum of digits, finding the maximum digit, and finding the minimum digit.

def calculator() -> None:
    """
    Receives a number and an action choice from the user, and then calls the appropriate function.
    """
    number = int(input('\nEnter the number: '))
    action = int(input('Enter the action (1 - digits sum, 2 - max digit, 3 - min digit): '))

    if action == 1:
        sum_digits(number)
    elif action == 2:
        max_digit(number)
    elif action == 3:
        min_digit(number)
    else:
        print('Input error, enter a number from 1 to 3.')


def sum_digits(number: int) -> None:
    """
    Calculates and prints the sum of the digits of the given number.
    :param number: Number to calculate the sum of digits.
    """
    total_sum = 0
    while number > 0:
        total_sum += number % 10
        number = number // 10
    print(f'The sum of digits is {total_sum}')


def max_digit(number: int) -> None:
    """
    Finds and prints the largest digit in the given number.
    :param number: Number to find the largest digit.
    """
    maximum = 0
    for digit in str(number):
        digit = int(digit)
        if digit > maximum:
            maximum = digit
    print(f'The largest digit is {maximum}')


def min_digit(number: int) -> None:
    """
    Finds and prints the smallest digit in the given number.
    :param number: Number to find the smallest digit.
    """
    minimum = 9
    for digit in str(number):
        digit = int(digit)
        if digit < minimum:
            minimum = digit
    print(f'The smallest digit is {minimum}')


# Main loop to run the calculator
while True:
    calculator()
