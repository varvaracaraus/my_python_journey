# File-Based Number Sum Calculator
# This script reads numbers from an input file, calculates their sum, and writes the sum to an output file.

import os


def read_numbers_from_file(file_path: str) -> list:
    """
    Reads numbers from a file and returns them as a list.

    Args:
        file_path (str): The path to the file containing numbers.

    Returns:
        list: A list of numbers read from the file.
    """
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers.extend(map(int, line.split()))
    return numbers


def calculate_sum(numbers: list) -> int:
    """
    Calculates the sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The sum of the numbers.
    """
    return sum(numbers)


def write_sum_to_file(file_path: str, result: int) -> None:
    """
    Writes the result to a file.

    Args:
        file_path (str): The path to the file where the result will be written.
        result (int): The result to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(str(result))


def main() -> None:
    """
    The main function to run the File-Based Number Sum Calculator.
    """
    input_file = 'numbers.txt'
    output_file = 'answer.txt'

    # Finding the absolute path of the input file
    input_file_path = os.path.abspath(input_file)

    # Checking if the input file exists and processing it
    if os.path.exists(input_file_path):
        numbers = read_numbers_from_file(input_file_path)
        result = calculate_sum(numbers)
        write_sum_to_file(output_file, result)
        print(f"The sum of numbers has been written to the file {output_file}")
    else:
        print(f"File {input_file} not found.")


# Running the main function
main()
