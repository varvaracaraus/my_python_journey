# Strong Password Validator
# This script validates user-created passwords, ensuring they meet specific strength criteria:
# at least one uppercase letter, one lowercase letter, three digits, and a minimum length of 8 characters.

while True:
    password = input("Create a password: ")
    has_uppercase = False
    has_lowercase = False
    has_digits = 0

    # Checking for password criteria
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digits += 1

    # Checking the length of the password
    is_long_enough = len(password) >= 8

    # Validating the password strength
    if has_uppercase and has_lowercase and has_digits >= 3 and is_long_enough:
        print("This is a strong password.")
        break
    else:
        print("Password is weak. Please try again.")
