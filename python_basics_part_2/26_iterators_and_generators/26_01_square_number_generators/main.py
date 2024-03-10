from square_generators import SquaresIterator, squares_generator, squares_expression

squares_iter = SquaresIterator(8)
for square in squares_iter:
    print(square)

for square in squares_generator(8):
    print(square)

squares_expr = squares_expression(8)
for square in squares_expr:
    print(square)
