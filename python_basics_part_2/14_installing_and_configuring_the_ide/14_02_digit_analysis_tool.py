# Digit Analysis Tool
# This script calculates and displays the sum of digits, the number of digits, and the difference
# between these two values for an input number.

def count_digits(num: int) -> int:
    """Count the number of digits in a given number.

    Args:
        num (int): The number to count digits in.

    Returns:
        int: The count of digits.
    """
    digit_count = 0
    while num > 0:
        num //= 10
        digit_count += 1
    return digit_count


def sum_digits(num: int) -> int:
    """Calculate the sum of digits in a given number.

    Args:
        num (int): The number to sum digits of.

    Returns:
        int: The sum of digits.
    """
    total_sum = 0
    while num > 0:
        last_digit = num % 10
        total_sum += last_digit
        num //= 10
    return total_sum


# Input and computation
number = int(input('Enter the number: '))
sum_of_digits = sum_digits(number)
count_of_digits = count_digits(number)
difference = sum_of_digits - count_of_digits

# Output
print('Sum of digits is:', sum_of_digits)
print('Number of digits:', count_of_digits)
print('Difference between sum and number of digits:', difference)
