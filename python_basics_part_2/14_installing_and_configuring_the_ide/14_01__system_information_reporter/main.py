# System Information Reporter
# This script retrieves and displays the operating system information and Python version details.
# It then writes this information into a text file named 'os_info.txt'.

import platform
import sys

# Retrieving OS and Python version information
system_info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)

# Displaying the system information
print(system_info)

# Writing the information to a file
with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(system_info)
