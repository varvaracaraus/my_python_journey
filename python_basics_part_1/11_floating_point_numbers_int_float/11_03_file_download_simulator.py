# File Download Simulator
# This script simulates the download of a file, taking into account the file size and the user's connection speed.
# It prints the progress of the download every second until the download is complete.

# Input for the file size and download speed
file_size_mb = float(input('Enter the file size to download in MB: '))
download_speed_mb = float(input('Enter your connection speed in MBps: '))
print()

# Initialize variables for time, downloaded amount, and remaining size
time_elapsed = 0
downloaded_amount = 0
remaining_size = file_size_mb

# Download simulation
while remaining_size > 0:
    time_elapsed += 1
    downloaded_amount += min(download_speed_mb, remaining_size)
    remaining_size -= download_speed_mb
    percent_downloaded = (downloaded_amount / file_size_mb) * 100

    # Print the download status
    print(f'{time_elapsed} sec passed. Downloaded {round(downloaded_amount)} of '
          f'{round(file_size_mb)} MB ({round(percent_downloaded)}%)')

# Final message when download is complete
if downloaded_amount >= file_size_mb:
    print(f'Download complete in {time_elapsed} seconds.')
