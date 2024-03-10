# Directory Information Analyzer
# This script analyzes a specified directory, providing the total size in kilobytes,
# number of subdirectories, and number of files in that directory.

import os


def get_directory_info(directory_path: str) -> tuple:
    """
    Gathers information about the specified directory, including its size, the number of subdirectories, and files.

    Args:
        directory_path (str): The path to the directory to analyze.

    Returns:
        tuple: Total size in kilobytes, number of subdirectories, and number of files.
    """
    total_size = 0
    total_subdirectories = 0
    total_files = 0

    for root, dirs, files in os.walk(directory_path):
        total_subdirectories += len(dirs)
        total_files += len(files)

        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    total_size_kb = total_size / 1024
    return total_size_kb, total_subdirectories, total_files


def main() -> None:
    """
    The main function that prompts the user for a directory path and prints its analyzed information.
    """
    directory_path = input("Enter the path to the directory: ")

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        size, subdirectories, files = get_directory_info(directory_path)

        print(f"\nDirectory size (in Kilobytes): {size:.2f}")
        print(f"Number of subdirectories: {subdirectories}")
        print(f"Number of files: {files}")
    else:
        print("The specified path does not exist or is not a directory.")


# Running the main function
main()
