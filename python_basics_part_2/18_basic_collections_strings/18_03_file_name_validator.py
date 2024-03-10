# File Name Validator
# This script checks if a user-input file name has a valid extension and doesn't start with a special symbol.

# Accepted file extensions
file_types = ['.txt', '.docx']

# List of special symbols
special_symbols = ['@', '№', '$', '%', '^', '&', '*', '()']

# Taking user input for a file name
file_name = input("File name: ")

# Extracting file extension
file_extension = file_name[-5:] if file_name.endswith('.docx') else file_name[-4:]

# Validating the file name and extension
if file_extension in file_types:
    if file_name[0] not in special_symbols:
        print("File named correctly.")
    else:
        print("Error: The name starts with an invalid symbol.")
else:
    print("Error: Incorrect file extension. Expected .txt or .docx.")
