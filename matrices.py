import numpy as np

def input_matrix(matrix_number):
    """Function to input a matrix from the user."""
    rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
    cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))
    print(f"Enter the elements of Matrix {matrix_number} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print("Error: Number of elements does not match the specified number of columns.")
            return None
        matrix.append(row)
    return np.array(matrix)

def add_matrices(mat1, mat2):
    """Function to add two matrices."""
    return mat1 + mat2

def subtract_matrices(mat1, mat2):
    """Function to subtract two matrices."""
    return mat1 - mat2

def multiply_matrices(mat1, mat2):
    """Function to multiply two matrices."""
    return np.dot(mat1, mat2)

def transpose_matrix(mat):
    """Function to transpose a matrix."""
    return np.transpose(mat)

def main():
    print("Matrix Operations using NumPy")
    
    # Input two matrices
    matrix1 = input_matrix(1)
    if matrix1 is None:
        return

    matrix2 = input_matrix(2)
    if matrix2 is None:
        return

    # Display the input matrices
    print("\nMatrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)

    # Choose an operation
    print("\nChoose an operation:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix 1")
    print("5. Transpose Matrix 2")
    
    choice = input("Enter the number of the operation you want to perform: ")

    if choice == '1':
        if matrix1.shape == matrix2.shape:
            result = add_matrices(matrix1, matrix2)
            print("\nResult of Addition:\n", result)
        else:
            print("Error: Matrices must have the same dimensions for addition.")

    elif choice == '2':
        if matrix1.shape == matrix2.shape:
            result = subtract_matrices(matrix1, matrix2)
            print("\nResult of Subtraction:\n", result)
        else:
            print("Error: Matrices must have the same dimensions for subtraction.")

    elif choice == '3':
        if matrix1.shape[1] == matrix2.shape[0]:
            result = multiply_matrices(matrix1, matrix2)
            print("\nResult of Multiplication:\n", result)
        else:
            print("Error: Number of columns in Matrix 1 must equal number of rows in Matrix 2 for multiplication.")

    elif choice == '4':
        result = transpose_matrix(matrix1)
        print("\nResult of Transposing Matrix 1:\n", result)

    elif choice == '5':
        result = transpose_matrix(matrix2)
        print("\nResult of Transposing Matrix 2:\n", result)

    else:
        print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()