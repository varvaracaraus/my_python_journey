# IP Address Validator
# This script validates the format of a user-input IP address, ensuring it consists of four numeric parts,
# each ranging from 0 to 255.

# Taking user input for an IP address
user_input = input("Enter an IP address: ")

# Splitting the input string by dots
address_parts = user_input.split('.')

# Validating the format and values of the IP address
if len(address_parts) != 4:
    print("An IP address consists of four numbers separated by dots.")
else:
    for part in address_parts:
        if not part.isdigit():
            print(f"{part} is not composed of digits.")
            break
        if not 0 <= int(part) <= 255:
            print(f"{part} is not within the valid range (0-255).")
            break
    else:
        print("The IP address is valid.")
