# Digit Swap and Sum Calculator
# This script prompts the user to input two numbers of specific lengths, swaps their first and last digits,
# and then calculates and prints the sum of these modified numbers.

def count_numbers(num: int) -> int:
    """
    Counts the number of digits in a given number.

    :param num: The number whose digits are to be counted.
    :return: The count of digits in num.
    """
    result = 0
    while num != 0:
        result += 1
        num //= 10
    return result


def input_handler(first_num_len: int, second_num_len: int) -> tuple:
    """
    Prompts the user to input two numbers with specific lengths.

    :param first_num_len: The length of the first number.
    :param second_num_len: The length of the second number.
    :return: A tuple containing the two numbers.
    """
    first_num = 0
    second_num = 0
    while count_numbers(first_num) != first_num_len:
        first_num = int(input(f"Type in the first number (len = {first_num_len}): "))
    while count_numbers(second_num) != second_num_len:
        second_num = int(input(f"Type in the second number (len = {second_num_len}): "))
    return first_num, second_num


def change_number(num: int, count: int) -> int:
    """
    Changes the number by swapping its first and last digits.

    :param num: The original number.
    :param count: The length of the number.
    :return: The number after swapping the first and last digits.
    """
    last_digit = num % 10
    first_digit = num // 10 ** (count - 1)
    between_digits = num % 10 ** (count - 1) // 10
    new_num = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return new_num


def main() -> None:
    first_num_len = 3
    second_num_len = 4

    first_num, second_num = input_handler(first_num_len, second_num_len)

    changed_first_num = change_number(first_num, first_num_len)
    changed_second_num = change_number(second_num, second_num_len)

    print(f"Changed first number: {changed_first_num}\n"
          f"Changed second number: {changed_second_num}\n"
          f"Sum: {changed_first_num + changed_second_num}")


# Run the main function
main()
