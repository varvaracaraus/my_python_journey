# Sandwich Method Decryption
# This script decrypts an encrypted message using the 'sandwich method'. It alternates characters from
# the start and end of the message to construct the original message.

# Input for the encrypted message
encrypted_msg = input('Enter the encrypted message: ')

# Initialize the strings for the left and right sides of the decrypted message
left_half = ''
right_half = ''
character_count = 0

# Decrypt the message
for char in encrypted_msg:
    character_count += 1
    if character_count % 2 == 1:
        left_half += char
    else:
        right_half = char + right_half

# Combine the halves to form the decrypted message
decrypted_msg = left_half + right_half

# Print the decrypted message
print('Decrypted message:', decrypted_msg)
