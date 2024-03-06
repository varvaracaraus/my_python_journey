# New Pirate Recruitment
# This script prompts potential pirates to enter the secret password. It then counts how
# many responded correctly with 'Savvy' or 'savvy'.

# Initialize the count of true pirates
true_pirates_count = 0

# Loop to check each potential pirate's password
for _ in range(10):
    pirate_password = input("Enter a real pirate's password: ")
    if pirate_password.lower() == 'savvy':
        true_pirates_count += 1

# Print the count of true pirates
print(f'Only {true_pirates_count} of you will become pirates!')
