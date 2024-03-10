# Number Reversal and Sum
# This script reverses two input numbers, adds them, and then reverses their sum.

def reverse_number(number: int) -> int:
    """
    Reverses the digits of a given number.

    :param number: The number to be reversed.
    :return: The reversed number.
    """
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number //= 10
    return reversed_number


# Get user input
n = int(input('\nEnter the first number: '))
k = int(input('Enter the second number: '))

# Reverse the numbers and calculate the reversed sum
reversed_n = reverse_number(n)
reversed_k = reverse_number(k)
total_sum = reversed_n + reversed_k
reversed_total_sum = reverse_number(total_sum)

# Print the results
print('\nFirst number reversed:', reversed_n)
print('Second number reversed:', reversed_k)
print('\nSum:', total_sum)
print('Reversed sum:', reversed_total_sum)
