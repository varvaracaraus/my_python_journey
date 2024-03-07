def smallest_divisor(input_number: int) -> int:
    """
    Finds the smallest divisor of a given number greater than 1.

    :param input_number: The number for which to find the smallest divisor.
    :return: The smallest divisor of the number, or the number itself if no smaller divisor is found.
    """
    local_divisor = 2
    while local_divisor <= input_number:
        if input_number % local_divisor == 0:
            return local_divisor
        local_divisor += 1


# User input for the number
number = int(input('Enter the number: '))

# Calculate and print the smallest divisor
divisor = smallest_divisor(number)
print('The smallest divisor other than one is:', divisor)
