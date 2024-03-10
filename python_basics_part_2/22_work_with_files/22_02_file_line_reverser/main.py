# File Line Reverser
# This script reads lines from a file and prints them in reverse order.

def reverse_lines(file_path: str) -> None:
    """
    Reads lines from a file and prints them in reverse order.

    Args:
        file_path (str): The path to the file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())


# Path to the file containing lines to be reversed
zen_file = 'zen.txt'

# Reversing and printing lines from the file
reverse_lines(zen_file)
