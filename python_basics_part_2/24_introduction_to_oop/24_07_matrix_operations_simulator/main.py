from matrix import Matrix

# Example usage of the Matrix class:

# Creating instances of the Matrix class
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Testing operations
print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Matrix Addition:")
print(m1.add(m2))

print("Matrix Subtraction:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Matrix Multiplication:")
print(m1.multiply(m3))

print("Matrix Transposition of Matrix 1:")
print(m1.transpose())
