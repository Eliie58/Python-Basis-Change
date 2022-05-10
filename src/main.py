import numpy as np
import plot_3d
import plot_2d


class Constant:
    DATA_TYPE_INT = "int"
    DATA_TYPE_FLOAT = "float"
    DATA_TYPE_STRICTLY_POSITIVE_INT = "int>=0"


def get_number(description, data_type):
    while True:
        try:
            if data_type == Constant.DATA_TYPE_INT:
                return int(input(description + " : "))
            elif data_type == Constant.DATA_TYPE_STRICTLY_POSITIVE_INT:
                value = int(input(description + " : "))
                if value <= 0:
                    raise ValueError
                return value
            elif data_type == Constant.DATA_TYPE_FLOAT:
                return float(input(description + " : "))
        except ValueError:
            print("Not a valid Number")


def capture_valid_matrix(dimension):
    matrix = np.zeros((dimension, dimension))
    for i in range(dimension):
        for j in range(dimension):
            matrix[i, j] = get_number("Enter the value in i={} and j={}".format(i, j), Constant.DATA_TYPE_FLOAT)
    print("Captured Matrix is : \n{}".format(matrix))
    if is_valid_matrix(matrix):
        return matrix
    return capture_valid_matrix(dimension)


# Check if matrix determinant is not 0
def is_valid_matrix(matrix):
    if np.linalg.det(matrix) == 0:
        print("Determinant of the matrix is 0, this is not a valid base matrix")
        return False
    return True


def capture_vector(dimension):
    vector = np.zeros(dimension)
    for i in range(dimension):
        vector[i] = get_number("Enter the value in i={}".format(i), Constant.DATA_TYPE_FLOAT)
    print("Captured Vector is : \n{}".format(vector))
    return vector


def change_basis(new_matrix, vector_canonical):
    matrix_inv = np.linalg.inv(new_matrix)
    return matrix_inv.dot(vector_canonical)


def main():
    dimension = get_number("Please enter the dimension of the space", Constant.DATA_TYPE_STRICTLY_POSITIVE_INT)
    print("Please input the values of the Origin Base Matrix")
    old_base = capture_valid_matrix(dimension)
    print("Please input the values of the Target Base Matrix")
    new_matrix = capture_valid_matrix(dimension)
    print("Please input the Vector coordinates in the Origin Base Matrix")
    old_vector = capture_vector(dimension)
    # First step, take the vector to its coordinates in Canonical Base
    vector_canonical = old_base.dot(old_vector)
    # Second step, change the coordinates to the target system
    new_vector = change_basis(new_matrix, vector_canonical)
    print(f'Original Vector is : \n{old_vector}')
    print(f'Vector in Canonical Base : \n{vector_canonical}')
    print(f'Vector in Target Base : \n{new_vector}')

    if dimension == 3:
        plot_3d.plot(old_base, new_matrix, old_vector, vector_canonical, new_vector)
    elif dimension == 2:
        plot_2d.plot(old_base, new_matrix, old_vector, vector_canonical, new_vector)


main()
