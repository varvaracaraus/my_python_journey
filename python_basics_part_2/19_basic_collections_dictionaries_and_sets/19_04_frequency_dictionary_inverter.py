# Frequency Dictionary Inverter
# This script takes a user-input text, creates a frequency dictionary of characters, and then inverts
# the dictionary to map frequencies to lists of characters with those frequencies.

def create_frequency_dict(text: str) -> dict:
    """
    Creates a frequency dictionary mapping each character to its frequency in the text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency_dict = {}
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict


def invert_frequency_dict(original_dict: dict) -> dict:
    """
    Inverts a frequency dictionary to map frequencies to lists of characters having those frequencies.

    Args:
        original_dict (dict): The original frequency dictionary.

    Returns:
        dict: An inverted dictionary mapping frequencies to lists of characters.
    """
    inverted_dict = {}
    for char, frequency in original_dict.items():
        if frequency not in inverted_dict:
            inverted_dict[frequency] = [char]
        else:
            inverted_dict[frequency].append(char)
    return inverted_dict


def main():
    # Taking user input
    input_text = input("Enter text: ")

    # Creating the original frequency dictionary
    original_frequency_dict = create_frequency_dict(input_text)

    print("\nOriginal frequency dictionary:")
    for char, frequency in sorted(original_frequency_dict.items()):
        print(f"{char} : {frequency}")

    # Creating the inverted frequency dictionary
    inverted_frequency_dict = invert_frequency_dict(original_frequency_dict)

    print("\nInverted frequency dictionary:")
    for frequency, chars in sorted(inverted_frequency_dict.items()):
        print(f"{frequency} : {chars}")


# Running the main function
main()
