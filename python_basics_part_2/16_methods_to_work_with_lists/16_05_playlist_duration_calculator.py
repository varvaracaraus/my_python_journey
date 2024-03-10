# Playlist Duration Calculator
# This script calculates the total playing time of a user-selected number of songs from the 'Violator' album.

# List of songs from the 'Violator' album with their durations
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

# Reading the number of songs to be chosen
my_songs = int(input('How many songs to choose? '))
total_duration = 0

# Selecting songs and calculating the total duration
for i in range(my_songs):
    song = input(f'Title of the {i + 1} song: ')
    for violator_song in violator_songs:
        if violator_song[0] == song:
            total_duration += violator_song[1]
            break

# Displaying the total playing time
print(f'Total playing time of songs: {total_duration:.2f} minutes')
