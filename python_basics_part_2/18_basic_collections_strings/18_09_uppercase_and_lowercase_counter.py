# Uppercase and Lowercase Counter
# This script counts the number of uppercase and lowercase letters in a user-provided string.

def count_uppercase_lowercase(input_text: str) -> tuple:
    """
    Counts the number of uppercase and lowercase letters in the input text.

    Args:
        input_text (str): The text to be analyzed.

    Returns:
        tuple: A tuple containing the count of uppercase letters and lowercase letters.
    """
    uppercase_letters = 0
    lowercase_letters = 0

    # Counting uppercase and lowercase letters
    for char in input_text:
        if char.isupper():
            uppercase_letters += 1
        elif char.islower():
            lowercase_letters += 1

    return uppercase_letters, lowercase_letters


# Taking user input for analysis
text = input("Enter a string for analysis: ")

# Getting counts of uppercase and lowercase letters
uppercase_count, lowercase_count = count_uppercase_lowercase(text)

# Displaying the results
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
