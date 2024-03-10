# File Processing with Error Logging
# This script processes a text file, counting the total number of characters,
# and logs errors for lines with less than three characters, optionally to a custom log file.

def process_file(input_file_path: str, custom_error_log_path: str = None) -> None:
    """
    Processes a file to count characters and logs errors for lines with less than three characters.

    Args:
        input_file_path (str): The path to the input file.
        custom_error_log_path (str, optional): The path to a custom error log file.
    """
    total_characters = 0

    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                line = line.strip()
                total_characters += len(line)

                if len(line) < 3 and line != "":
                    raise ValueError(f"Less than three characters in line {line_number}.")

            except ValueError as e:
                print(f"Error: {e}")
                if custom_error_log_path:
                    with open(custom_error_log_path, 'a', encoding='utf-8') as error_log:
                        error_log.write(f"Error: {e}\n")

    print(f"\nTotal number of characters: {total_characters}")


# Paths to the input file and the error log file
file_path = "people.txt"
error_log_path = "errors.log"

# Processing the file with error logging
process_file(file_path, error_log_path)
