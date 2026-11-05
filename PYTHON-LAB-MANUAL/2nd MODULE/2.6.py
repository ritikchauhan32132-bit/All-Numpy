"""

2.6	Create a 2x3 matrix using NumPy:

    •	Access the element at first row, second column.
    •	Replace the last row with [7, 8, 9].
    •	Find the transpose of the matrix.


"""
import numpy as np
matrix = np.arange(6).reshape(2,3)

print(matrix[0,1])
matrix[1] = [7,8,9]
print(matrix)
print(f"<=== Transpose ===>\n{matrix.T}")