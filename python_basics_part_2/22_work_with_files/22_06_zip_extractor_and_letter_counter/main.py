# Zip Extractor and Letter Counter
# This script extracts content from a ZIP file, counts letter frequencies in a text file,
# and prints the letter statistics in a specified sort order.

import os
import zipfile


def extract_zip(zip_path: str, extract_path: str) -> None:
    """
    Extracts all files from a ZIP file into a specified directory.

    Args:
        zip_path (str): The path to the ZIP file.
        extract_path (str): The path to the directory where files will be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


def count_letters(file_path: str) -> dict:
    """
    Counts the frequency of each letter in a file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        dict: A dictionary mapping each letter to its frequency.
    """
    letter_counts = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts


def print_letter_statistics(letter_counts: dict, sort_order: str = 'ascending') -> None:
    """
    Prints letter frequencies in a sorted order.

    Args:
        letter_counts (dict): A dictionary of letter frequencies.
        sort_order (str): The order in which to sort the letters ('ascending' or 'descending').
    """
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=(sort_order == 'descending'))

    for letter, count in sorted_letter_counts:
        print(f"{letter}: {count}")


# Path to the ZIP file and the extraction directory
zip_path_outer = 'voyna-i-mir.zip'
extract_path_outer = 'extracted'

# Extracting the ZIP file
extract_zip(zip_path_outer, extract_path_outer)

# Path to the extracted text file
file_path_outer = os.path.join(extract_path_outer, 'voyna-i-mir.txt')

# Counting letter frequencies
letter_counts_outer = count_letters(file_path_outer)

# Printing letter statistics in descending order
print_letter_statistics(letter_counts_outer, sort_order='descending')
