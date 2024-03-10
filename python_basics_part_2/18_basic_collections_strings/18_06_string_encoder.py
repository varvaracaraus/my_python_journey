# String Encoder
# This script encodes a string by compressing consecutive identical characters into a single character
# followed by its count.

def encode_string(input_string: str) -> str:
    """
    Encodes the given string by compressing consecutive identical characters.

    Args:
        input_string (str): The string to be encoded.

    Returns:
        str: The encoded string.
    """
    encoded_result = []
    character_count = 1

    # Encoding the string
    for i in range(len(input_string)):
        if i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            character_count += 1
        else:
            encoded_result.append(input_string[i] + str(character_count))
            character_count = 1

    return ''.join(encoded_result)


# Taking user input for the string
user_input = input("Enter a string: ")

# Getting the encoded string
encoded_output = encode_string(user_input)

# Displaying the encoded string
print(f'Encoded string: {encoded_output}')
