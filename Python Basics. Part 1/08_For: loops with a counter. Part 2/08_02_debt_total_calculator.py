# Debt Total Calculator
# This script asks for the total number of debtors and then queries every fifth debtor about their debt amount.
# It calculates and prints the total debt amount based on these inputs.

# Input for the number of debtors
number_of_debtors = int(input('Enter the number of debtors: '))

# Initialize the total debt
total_debt = 0

# Loop through every fifth debtor
for debtor_number in range(5, number_of_debtors + 1, 5):
    print(f'Debtor No. {debtor_number}')
    debt = int(input('How much do you owe? '))
    total_debt += debt

# Print the total debt amount
print('Total debt amount:', total_debt)
