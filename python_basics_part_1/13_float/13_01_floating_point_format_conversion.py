# Floating-Point Format Conversion
# This script takes a number as input and converts it into a floating-point format (scientific notation).

number = float(input('Enter the number: '))

# Handle the case where the number is zero
if number == 0:
    print("Floating point format: x = 0")
else:
    exponent = 0
    # Adjust the number and exponent for numbers greater than or equal to 10
    while number >= 10:
        exponent += 1
        number /= 10
    # Adjust for numbers less than 1
    while number < 1:
        exponent -= 1
        number *= 10

    # Print the result in scientific notation
    print(f"Floating point format: x = {round(number, 4)} * 10 ** {exponent}")
