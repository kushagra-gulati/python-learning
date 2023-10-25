import numpy as np
# Let's create and cast a list of list to generate 2-D array
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print( my_matrix )
# Two-dimensional array from Matrix
matrix_one = np.array(my_matrix) # type: ignore
print(matrix_one)