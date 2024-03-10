# Randomized Number Writer with File Output
# This script allows the user to input numbers which are then appended to a file.
# The process continues until the sum of numbers reaches 777 or a random failure occurs.

import random


def read_number() -> int:
    """
    Prompts the user to enter a number and returns it. Repeats the prompt if the input is not a valid integer.

    Returns:
        int: The number entered by the user.
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter only a number.")


def write_to_file(file_name: str, number: int) -> None:
    """
    Writes a number to a file.

    Args:
        file_name (str): The name of the file to write to.
        number (int): The number to write to the file.

    Raises:
        Exception: If an error occurs while writing to the file.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(f"{number}\n")
    except Exception as e:
        raise Exception(f"Error writing to file: {e}")


def main() -> None:
    """
    The main function of the script. Manages the process of reading, writing numbers, and checks the exit condition.
    """
    file_name = "out_file.txt"
    total_sum = 0

    # Resetting or creating the file
    with open(file_name, 'w'):
        pass

    while total_sum < 777:
        try:
            current_number = read_number()
            total_sum += current_number
            write_to_file(file_name, current_number)

            if random.randint(1, 13) == 1:
                print("You encountered a failure!")
                break

        except Exception as e:
            print(f"Error: {e}")
            break

    if total_sum >= 777:
        print("You have successfully met the exit condition for the loop!")

    # Reading and displaying the file contents
    with open(file_name, 'r') as file:
        print(f"Contents of the file {file_name}:\n{file.read()}")


# Running the main function
main()
