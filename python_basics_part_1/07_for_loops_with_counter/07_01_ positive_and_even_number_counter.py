# Positive and Even Number Counter
# This script prompts the user to enter ten numbers and then counts how many of those numbers are both
# positive and even.

# Initialize the counter for positive and even numbers
positive_even_count = 0

# Loop to get ten numbers and count the positive, even ones
for _ in range(10):
    number = int(input('Enter the number: '))
    if number % 2 == 0 and number > 0:
        positive_even_count += 1

# Print the result
print('Number of positive and even numbers:', positive_even_count)
