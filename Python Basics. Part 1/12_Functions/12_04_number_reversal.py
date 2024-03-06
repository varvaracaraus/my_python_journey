# Number Reversal
# This script takes a sequence of positive integers from the user and prints each number in reverse order.
# The process continues until the user inputs 0, at which point the program terminates.

def reverse_number(num: int) -> None:
    """
    Reverses the digits of the given number and prints the result.

    :param num: The number to be reversed.
    """
    reversed_number = 0
    while num != 0:
        last_digit = num % 10
        reversed_number = reversed_number * 10 + last_digit
        num = num // 10
    print(f'Reversed number: {reversed_number}')


# Main loop to process user input
while True:
    user_input = int(input('\nInput a sequence of positive integers: '))
    if user_input == 0:
        print('Program completed!')
        break
    else:
        reverse_number(user_input)
