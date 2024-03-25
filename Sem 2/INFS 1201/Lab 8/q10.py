##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 9

def matrixProduct(A, B):
    'Returns the matrix product AB for given rectangular matrices A and B'
    m = len(A)
    n = len(B)          # n = len(A[0]) = len(B)
    p = len(B[0])       # Given B is a rectangular matrix

    C = []
    for i in range(m):
        C.append([])
        for j in range(p):
            sum = 0
            for k in range(n):
                sum += A[i][k] * B[k][j]
            C[i].append(sum)
    
    return C





'''
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix2 = [
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(matrixProduct(matrix1, matrix2))
'''