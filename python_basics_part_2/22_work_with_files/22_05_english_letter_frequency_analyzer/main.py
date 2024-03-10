# English Letter Frequency Analyzer
# This script analyzes the frequency of English letters in a text file and outputs the results sorted by frequency.

import os
import os.path


def is_english_letter(char: str) -> bool:
    """
    Checks if a character is an English letter.

    Args:
        char (str): The character to check.

    Returns:
        bool: True if the character is an English letter, False otherwise.
    """
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'


def sort_key(item: tuple) -> tuple:
    """
    Sort key for sorting letters by frequency and alphabetically.

    Args:
        item (tuple): The item (letter, frequency) to be sorted.

    Returns:
        tuple: A tuple for sorting purpose.
    """
    return -item[1], item[0]


def analyze_frequency(in_file_path: str, out_file_path: str) -> None:
    """
    Analyzes the frequency of English letters in a file and writes the sorted results to another file.

    Args:
        in_file_path (str): The path to the input text file.
        out_file_path (str): The path to the output file for writing frequency analysis.
    """
    if not os.path.isfile(in_file_path):
        print(f"The file {in_file_path} does not exist.")
        return

    letter_frequencies = {}
    total_letters = 0

    with open(in_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    for char in text:
        if is_english_letter(char):
            char_lower = char.lower()
            letter_frequencies[char_lower] = letter_frequencies.get(char_lower, 0) + 1
            total_letters += 1

    letter_percentages = {letter: frequency / total_letters for letter, frequency in letter_frequencies.items()}
    sorted_letter_percentages = sorted(letter_percentages.items(), key=sort_key)

    with open(out_file_path, 'w', encoding='utf-8') as output_file:
        for letter, percentage in sorted_letter_percentages:
            output_file.write(f"{letter} {percentage:.3f}\n")


# Paths to the input and output files
input_file_path = 'text.txt'
output_file_path = 'analysis.txt'

# Running the frequency analysis
analyze_frequency(input_file_path, output_file_path)
