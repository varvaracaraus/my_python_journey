# Cyclic Shift Checker
# This script checks if the first string can be obtained from the second string by performing a cyclic shift.

# Taking user inputs for two strings
first_string = input("First string: ")
second_string = input("Second string: ")

# Checking if cyclic shift is possible
if len(first_string) != len(second_string):
    print("The first string cannot be obtained from the second one by cyclic shift.")
else:
    combined_string = ''.join([second_string, second_string])
    shift_value = combined_string.find(first_string)
    if shift_value != -1:
        print(f"The first string can be obtained from the second one by a shift of {shift_value}.")
    else:
        print("The first string cannot be obtained from the second one by cyclic shift.")
