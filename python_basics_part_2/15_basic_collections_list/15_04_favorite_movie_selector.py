# Favorite Movie Selector
# This script allows users to add movie titles to their favorites from a predefined list.
# If the movie is not in the list, it notifies the user.

# Predefined list of movies
movies = ['Die Hard', 'Back to the Future', 'Taxi Driver', 'Leon',
          'Bohemian Rhapsody', 'Sin City', 'Memento', 'The Departed',
          'The Village']
favorites = ''

# Reading the number of movies the user wants to add
quantity = int(input('How many movies do you want to add? '))

# Adding movies to favorites
for _ in range(quantity):
    film = input('Enter movie title: ')
    if film in movies:
        favorites += film + ', '
    else:
        print(f"We don't have the {film} movie :(")

# Cleaning up the trailing comma and space in the favorites string
if favorites:
    favorites = favorites.rstrip(', ')

# Displaying the list of favorite movies
print('Your list of favorite films:', favorites)
