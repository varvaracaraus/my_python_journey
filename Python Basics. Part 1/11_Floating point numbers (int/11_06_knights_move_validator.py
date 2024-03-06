# Knight's Move Validator
# This script determines if a move made by a knight in chess is valid based on input coordinates.
# The chessboard is represented in a 0.8x0.8 grid, and the user provides coordinates for the knight and target position.

while True:
    print('\nEnter knight location:')
    knight_lat = float(input('Latitude (0 to 0.8): '))
    knight_long = float(input('Longitude (0 to 0.8): '))

    print('\nEnter target location:')
    target_lat = float(input('Latitude (0 to 0.8): '))
    target_long = float(input('Longitude (0 to 0.8): '))

    if 0 <= knight_lat <= 0.8 and 0 <= knight_long <= 0.8 and 0 <= target_lat <= 0.8 and 0 <= target_long <= 0.8:
        k_lat_coord = int(knight_lat * 10)
        k_long_coord = int(knight_long * 10)
        t_lat_coord = int(target_lat * 10)
        t_long_coord = int(target_long * 10)

        print(f'\nThe knight is in square ({k_lat_coord}, {k_long_coord}).')
        print(f'The point is in square ({t_lat_coord}, {t_long_coord}).')

        lat_diff = abs(t_lat_coord - k_lat_coord)
        long_diff = abs(t_long_coord - k_long_coord)

        if (long_diff == 1 and lat_diff == 2) or (long_diff == 2 and lat_diff == 1):
            print('Yes, the knight can move to this point.')
        else:
            print("No, the knight can't move to this point.")
        break
    else:
        print('\nInvalid coordinates. Please enter coordinates between 0 to 0.8.')
