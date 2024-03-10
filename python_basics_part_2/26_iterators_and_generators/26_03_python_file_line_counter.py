import os
from typing import Generator


def count_lines_in_python_files(target_directory: str) -> Generator[tuple[str, int], None, None]:
    """
    A generator function that iterates over Python files in the specified directory,
    counts the number of non-empty and non-comment lines in each file, and yields
    this count along with the file name. Files are processed in alphabetical order.

    :param target_directory: The directory to search for Python files.
    :return: A generator that yields a tuple containing the file name and the line count.
    """
    python_files = []
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    for current_file_path in sorted(python_files):
        with open(current_file_path, 'r', encoding='utf-8') as f:
            lines = [line for line in f if line.strip() and not line.strip().startswith('#')]
            yield current_file_path, len(lines)


directory = '/Users/varvaracaraus/PycharmProjects/my_python_journey/python_basics_part_2/26_iterators_and_generators'
for file_path, line_count in count_lines_in_python_files(directory):
    print(f"{file_path}: {line_count} lines")
