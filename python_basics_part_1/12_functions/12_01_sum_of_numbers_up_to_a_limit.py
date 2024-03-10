# Sum of Numbers Up to a Limit
# This script defines a function that calculates and prints the sum of all natural numbers up to a specified limit.
# The script prompts the user for the limit and then uses the function to compute the sum.

def sum_n(limit: int) -> None:
    """
    Calculate and print the sum of all natural numbers from 1 to the limit.

    :param limit: The upper limit for the sum, must be a positive integer.
    :type limit: int
    :return: None
    """
    total = 0
    if limit > 0:
        for number in range(1, limit + 1):
            total += number
        print(f'I know that the sum of the numbers from 1 to {limit} is {total}')
    else:
        print('Input error, run again and enter a positive integer.')


# Prompt for the upper limit
user_input = int(input('\nEnter the number: '))

# Call the function with the provided limit
sum_n(user_input)
