# System Login
# This script greets the user and informs them about the lack of system access.

# Get the user's first name
first_name = input('Enter your name: ')

# Greeting message
greeting = 'Good morning, '
print(greeting, first_name)

# Access denial information
access_denied_message = "Unfortunately, you do not have access to the system."
contact_admin_message = "Please, contact the system administrator."

# Print the access denial information
print(access_denied_message)
print(contact_admin_message)
