# Q Write Python program for multiplication of two matrix

def matrix_multiplication(matrix_1, matrix_2):
    rows1 = len(matrix_1)
    cols1 = len(matrix_1[0])
    rows2 = len(matrix_2)
    cols2 = len(matrix_2[0])

    # Check if matrix multiplication is possible
    if cols1 != rows2:
        print("Matrix multiplication is not possible.")
        return None

    # Initialize the result matrix
    results = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                results[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return results


# input
matrix_1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix_2 = [[10, 11],
           [12, 13],
           [14, 15]]

result = matrix_multiplication(matrix_1, matrix_2)
if result is not None:
    for row in result:
        print(row)

# output:
# [76, 82]
# [184, 199]
# [292, 316]