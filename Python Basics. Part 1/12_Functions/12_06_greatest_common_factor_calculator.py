# Greatest Common Factor Calculator
# This script calculates the greatest common factor of two numbers using the Euclidean algorithm.

def calculate_gcf(num1: int, num2: int) -> None:
    """
    Calculates and prints the greatest common factor of two given numbers.

    :param num1: The first number.
    :param num2: The second number.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    print(f'The greatest common factor is: {num1}')


# Get user input
first_number = int(input('Enter the 1st number: '))
second_number = int(input('Enter the 2nd number: '))

# Call the function with user input
calculate_gcf(first_number, second_number)
