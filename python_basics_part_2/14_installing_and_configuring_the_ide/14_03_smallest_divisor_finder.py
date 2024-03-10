# Smallest Divisor Finder
# This script calculates and displays the smallest divisor of a given number, other than one.

def smallest_divisor(input_number: int) -> int:
    """Find the smallest divisor of a given number, excluding one.

    Args:
        input_number (int): The number for which the smallest divisor is to be found.

    Returns:
        int: The smallest divisor of the input number.
    """
    local_divisor = 2
    while local_divisor <= input_number:
        if input_number % local_divisor == 0:
            return local_divisor
        local_divisor += 1


# Taking input from the user and computing the smallest divisor
number = int(input('Enter the number: '))
divisor = smallest_divisor(number)

# Displaying the result
print('The smallest divisor other than one is:', divisor)
