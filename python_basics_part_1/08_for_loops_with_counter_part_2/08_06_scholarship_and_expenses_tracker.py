# Scholarship and Expenses Tracker
# This script calculates and displays a student's monthly expenses and overdraft for 10 months.
# The student receives an educational grant each month, but their accommodation expenses increase by 3% monthly.

# Input for the monthly educational grant and initial accommodation expenses
educational_grant = int(input('Enter your scholarship: '))
monthly_expenses = int(input('Enter your initial accommodation expenses: '))
monthly_overdraft = monthly_expenses - educational_grant

# Display the first month's expenses and overdraft
print(f'1st month expenses = {round(monthly_expenses, 2)} Overdraft = {round(monthly_overdraft, 2)}')

# Calculate and display expenses and overdraft for subsequent months
for month in range(2, 11):
    monthly_expenses *= 1.03  # Monthly expenses increase by 3%
    monthly_overdraft += (monthly_expenses - educational_grant)
    print(f'{month}th month expenses = {round(monthly_expenses, 2)} Overdraft = {round(monthly_overdraft, 2)}')

# Print the total amount needed to cover the overdraft
print(f'You need to ask your parents for ${round(monthly_overdraft, 2)}')
