# Recursive Number Printer
# This script prints all numbers from 1 up to a user-input number using recursion.

def print_numbers_up_to(num: int) -> None:
    """
    Recursively prints numbers from 1 up to the specified number.

    Args:
        num (int): The number up to which to print.
    """
    if num > 1:
        print_numbers_up_to(num - 1)
    print(num)


# Taking user input for the number
numb = int(input("Enter a number: "))

# Printing numbers up to the user-input number
print_numbers_up_to(numb)
