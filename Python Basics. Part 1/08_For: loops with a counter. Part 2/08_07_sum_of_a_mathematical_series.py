# Sum of a Mathematical Series
# This script calculates the sum of a series defined by the formula ((-1) ^ n) * (1 / 2 ^ n)
# for n ranging from 0 to the user-defined number.

# Input for the number of terms in the series
number_of_terms = int(input('Enter the number of terms: '))

# Initialize the sum of the series
series_sum = 0

# Calculate the sum of the series
for term in range(number_of_terms):
    element = ((-1) ** term) * (1 / (2 ** term))
    series_sum += element

# Print the sum of the series
print('Sum of the series:', series_sum)
