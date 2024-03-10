# Song Duration Calculator
# This script calculates the total duration of a selected list of songs using a dictionary of song names and
# their durations.

def calculate_total_duration(song_dict: dict, select_songs: list) -> float:
    """
    Calculates the total duration of selected songs.

    Args:
        song_dict (dict): Dictionary with song titles as keys and durations as values.
        select_songs (list): List of song titles to calculate the total duration.

    Returns:
        float: The total duration of the selected songs.
    """
    tot_duration = 0
    for song in select_songs:
        tot_duration += song_dict.get(song, 0)
    return tot_duration


# Dictionary of songs with their durations
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# Collecting user input for the number of songs to choose
num_of_songs = int(input("How many songs to choose? "))

# Collecting user input for the song names
selected_songs = []
for i in range(num_of_songs):
    song_name = input(f"Name of {i + 1} song: ")
    selected_songs.append(song_name)

# Calculating the total duration of selected songs
total_duration = calculate_total_duration(violator_songs, selected_songs)

# Displaying the total duration
print(f"Total duration of selected songs: {total_duration:.2f} minutes")
