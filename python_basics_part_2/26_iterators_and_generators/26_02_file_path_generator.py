import os
from typing import Iterator


def generate_file_paths(directory: str = '/') -> Iterator[str]:
    """
    Generates paths of all files in the given directory and its subdirectories.

    :param directory: Path to the directory to be traversed, defaults to the root directory.
    :return: An iterator that yields the paths of the files as strings.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


directory_path = ('/Users/varvaracaraus/PycharmProjects/my_python_journey/python_basics_part_2'
                  '/26_iterators_and_generators')

for file_path in generate_file_paths(directory_path):
    print(file_path)
