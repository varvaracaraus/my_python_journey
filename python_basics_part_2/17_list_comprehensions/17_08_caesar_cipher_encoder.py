# Caesar Cipher Encoder
# This script encrypts a message using the Caesar cipher method, shifting each letter by a specified number of places.

def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypts the given text using the Caesar cipher technique.

    Args:
        text (str): The text to be encrypted.
        shift (int): The number of places to shift each letter.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Encrypting each character
    for char in text:
        if char in alphabet:
            shifted_index = (alphabet.index(char) + shift) % 26
            encrypted_char = alphabet[shifted_index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


# Taking user input for the message and shift value
message = input('Enter the message: ')
shift_value = int(input('Enter the shift value: '))

# Encrypting the message
encrypted_message = caesar_cipher(message, shift_value)

# Displaying the encrypted message
print(f'Encrypted message: {encrypted_message}')
