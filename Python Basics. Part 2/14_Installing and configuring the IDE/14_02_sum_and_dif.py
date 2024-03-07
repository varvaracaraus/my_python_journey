def digit_count(num: int) -> int:
    """
    Counts the number of digits in a given integer.

    :param num: Integer to count digits of.
    :return: Count of digits.
    """
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


def digits_sum(num: int) -> int:
    """
    Calculates the sum of the digits of a given integer.

    :param num: Integer to calculate the digits sum of.
    :return: Sum of the digits.
    """
    total_sum = 0
    while num > 0:
        last_digit = num % 10
        total_sum += last_digit
        num //= 10
    return total_sum


# User input for the number
number = int(input('Enter the number: '))

# Calculate sum of digits and count of digits
sum_of_digits = digits_sum(number)
count_of_digits = digit_count(number)

# Calculate the difference between sum and count of digits
difference = sum_of_digits - count_of_digits

# Print the results
print('Sum of digits is:', sum_of_digits)
print('Number of digits:', count_of_digits)
print('Difference between sum and number of digits:', difference)
