import platform
import sys

# This script collects information about the operating system and the Python version,
# then writes this information to a file named 'os_info.txt'.

# Gathering OS and Python version information.
info = (
    f"OS info is \n{platform.uname()}\n\n"  # Retrieves detailed OS information.
    f"Python version is {sys.version} {platform.architecture()}"  # Gets the current Python version and architecture.
)

print(info)

# Writing the gathered information to 'os_info.txt'.
with open('14_01_os_info/os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
