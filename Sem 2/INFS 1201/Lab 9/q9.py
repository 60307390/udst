##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 9

def matrix_transpose(A):
    'Returns the transpose Aᵀ, given a matrix A'
    A_T = []
    for i in range(len(A[0])):  # Given A is a rectangular matrix
        A_T.append([])

    for i in range(len(A)):
        for j in range(len(A[i])):
            A_T[j].append(A[i][j])
    return A_T





'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

print(matrix_transpose(matrix))
'''