# Prime Number Counter
# This script asks the user to input a sequence of integers and then counts how many of these
# integers are prime numbers. A prime number is a natural number greater than 1 that has no
# positive divisors other than 1 and itself.

# Input for the number of integers in the sequence
number_of_integers = int(input('Enter the number of integers: '))
prime_numbers_count = 0

# Loop through each number in the sequence
for i in range(number_of_integers):
    number = int(input(f'Enter number {i + 1}: '))
    # Check if the number is prime
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            prime_numbers_count += 1

# Print the total count of prime numbers in the sequence
print(f"The number of prime numbers in the sequence: {prime_numbers_count}")
