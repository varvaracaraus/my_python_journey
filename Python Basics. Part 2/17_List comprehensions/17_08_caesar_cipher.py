def caesar_cipher(text, shift):
    """
    Encrypts the given text using the Caesar cipher method.

    :param text: The plaintext message to be encrypted.
    :param shift: The number of positions each letter in the plaintext is shifted.
    :return: The encrypted message.
    """
    encrypted_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Iterate through each character in the text
    for char in text:
        # Check if the character is in the alphabet
        if char in alphabet:
            # Find the new shifted position of the character and add to the encrypted text
            shifted_index = (alphabet.index(char) + shift) % 26
            encrypted_char = alphabet[shifted_index]
            encrypted_text += encrypted_char
        else:
            # If the character is not in the alphabet (like spaces, punctuation), add it as is
            encrypted_text += char

    return encrypted_text


# User input for the message and shift value
message = input('Enter the message: ')
shift_value = int(input('Enter the shift value: '))

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(message, shift_value)

# Print the encrypted message
print(f'Encrypted message: {encrypted_message}')
