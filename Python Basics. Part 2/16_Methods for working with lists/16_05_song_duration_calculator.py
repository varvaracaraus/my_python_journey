# Song Duration Calculator
# This script allows the user to select a certain number of songs from a predefined list and calculates the
# total playing time.

# List of songs with their durations
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# User input for the number of songs to choose
my_songs = int(input('How many songs to choose? '))

# Initialize a variable to hold the total duration
count = 0

# Loop to let the user select songs
for i in range(my_songs):
    song = input(f'Title of the {i + 1} song: ')
    # Check if the entered song is in the list and add its duration
    for violator_song in violator_songs:
        if violator_song[0] == song:
            count += violator_song[1]
            break

# Print the total playing time of the selected songs
print(f'Total playing time of songs: {count:.2f} minutes')
