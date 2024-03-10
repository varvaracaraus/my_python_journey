# Financial Report
# This script calculates and compares the income dynamics across two halves of a financial year.

# Input for quarterly incomes
first_quarter_income = int(input('Enter the first quarter income: '))
second_quarter_income = int(input('Enter the second quarter income: '))
third_quarter_income = int(input('Enter the third quarter income: '))
fourth_quarter_income = int(input('Enter the fourth quarter income: '))

# Calculate the sum of incomes for the first two and last two quarters
income_first_half = first_quarter_income + second_quarter_income
income_second_half = third_quarter_income + fourth_quarter_income

# Calculate the income dynamics
income_dynamics = income_first_half / income_second_half

# Print the income dynamics
print('Income dynamics: ', income_dynamics)
