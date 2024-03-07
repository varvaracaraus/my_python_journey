# Favorite Movies Selection
# This script allows the user to add movies to their list of favorites from a predefined list of movies.

# List of available movies
movies = ['Die Hard', 'Back to the Future', 'Taxi Driver', 'Leon',
          'Bohemian Rhapsody', 'Sin City', 'Memento', 'The Departed',
          'The Village']

# Ask user how many movies they want to add
quantity = int(input('How many movies do you want to add? '))

# Initialize an empty list for favorites
favorites = []

# Add user-selected movies to the favorites list if they exist in the available movies list
for _ in range(quantity):
    film = input('Enter movie title: ')
    if film in movies:
        favorites.append(film)
    else:
        print(f"We don't have the {film} movie :(")

# Convert the list of favorites to a comma-separated string
favorites_str = ', '.join(favorites)

# Print the list of favorite movies
print('Your list of favorite films:', favorites_str)
