import os


def error_log_generator(log_file_path: str):
    """A generator function that yields lines containing 'ERROR' from a log file.

    Args:
        log_file_path (str): The path to the log file.

    Yields:
        str: The next line containing 'ERROR'.
    """
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


data_directory = ('/Users/varvaracaraus/PycharmProjects/my_python_journey/python_basics_part_2'
                  '/26_iterators_and_generators/26_05_error_log_processor/data')
input_file_name = 'work_logs.txt'
output_file_name = 'output.txt'

input_file_path = os.path.join(data_directory, input_file_name)
output_file_path = os.path.join(data_directory, output_file_name)

if not os.path.exists(input_file_path):
    print(f"Input file {input_file_path} does not exist.")
else:
    with open(output_file_path, 'w', encoding='utf-8') as output:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
    print("The file was processed successfully.")
