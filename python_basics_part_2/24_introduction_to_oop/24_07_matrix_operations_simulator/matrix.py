class Matrix:
    """Represents a mathematical matrix."""

    def __init__(self, rows: int, cols: int):
        """
        Initialize a new matrix with given rows and columns.

        Args:
            rows (int): The number of rows.
            cols (int): The number of columns.
        """
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self) -> str:
        """Return a string representation of the matrix."""
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def add(self, other: 'Matrix') -> 'Matrix':
        """
        Add another matrix to this matrix.

        Args:
            other (Matrix): The matrix to be added.

        Returns:
            Matrix: The resulting matrix after addition.

        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other: 'Matrix') -> 'Matrix':
        """
        Subtract another matrix from this matrix.

        Args:
            other (Matrix): The matrix to be subtracted.

        Returns:
            Matrix: The resulting matrix after subtraction.

        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other: 'Matrix') -> 'Matrix':
        """
        Multiply this matrix with another matrix.

        Args:
            other (Matrix): The matrix to multiply with.

        Returns:
            Matrix: The resulting matrix after multiplication.

        Raises:
            ValueError: If the number of columns in this matrix is not equal to the number of rows in the other matrix.
        """
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self) -> 'Matrix':
        """
        Transpose this matrix.

        Returns:
            Matrix: The transposed matrix.
        """
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result
