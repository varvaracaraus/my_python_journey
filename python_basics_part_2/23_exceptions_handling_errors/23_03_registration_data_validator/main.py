# Registration Validator and Logger
# This script processes registration data from a file, validating each registration entry,
# and categorizes them into valid and invalid entries, writing them to separate output files.

from typing import Optional


def validate_registration(name: str, email: str, age: str) -> Optional[str]:
    """
    Validates a registration entry.

    Args:
        name (str): The name to validate.
        email (str): The email to validate.
        age (str): The age to validate.

    Returns:
        Optional[str]: An error message if the validation fails, otherwise None.
    """
    try:
        if not name.isalpha():
            raise ValueError("\tThe 'Name' field contains non-alphabetic characters")
        elif '@' not in email or '.' not in email:
            raise ValueError("\tThe 'Email' field does not contain @ and dot")
        elif not (10 <= int(age) <= 99):
            raise ValueError("\tThe 'Age' field does not represent a number between 10 and 99")
    except ValueError as e:
        return str(e)

    return None


def process_registrations(input_file_path: str, good_file_path: str, bad_file_path: str) -> None:
    """
    Processes registration entries from an input file and writes valid and invalid entries to separate files.

    Args:
        input_file_path (str): The file containing registration entries.
        good_file_path (str): The file to write valid entries.
        bad_file_path (str): The file to write invalid entries.
    """
    with open(input_file_path, 'r') as file, \
            open(good_file_path, 'w') as good_file, \
            open(bad_file_path, 'w') as bad_file:
        for line in file:
            try:
                name, email, age = line.split()
                validation_result = validate_registration(name, email, age)
                if validation_result:
                    bad_file.write(f"{line.strip()}\t{validation_result}\n")
                else:
                    good_file.write(line)
            except ValueError:
                bad_file.write(f"{line.strip()}\tNot all three fields are present\n")


# Global variables for file paths
input_file = 'registrations.txt'
good_output_file = 'registrations_good.log'
bad_output_file = 'registrations_bad.log'

# Processing the registration entries
process_registrations(input_file, good_output_file, bad_output_file)
