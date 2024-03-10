# Yearly Average Salary Calculator
# This script prompts the user to input monthly salaries for each month of the year and then calculates
# and prints the average yearly salary.

# Initialize the total yearly salary
total_yearly_salary = 0

# Loop to collect monthly salaries and accumulate the total
for month in range(1, 13):
    monthly_salary = int(input(f'Enter salary for month {month}: '))
    total_yearly_salary += monthly_salary

# Calculate the average salary
average_salary = total_yearly_salary / 12

# Print the average yearly salary
print('Yearly average salary:', average_salary)
