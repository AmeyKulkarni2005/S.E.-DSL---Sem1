'''Write a python program to compute following computation on
matrix:
     a) Addition of two matrices
     b) Subtraction of two matrices
     c) Multiplication of two matrices
     d) Transpose of a matrix'''


i = int(input("Enter no. of rows of matrix1: "))
j = int(input("Enter no. of columns of matrix1: "))
matrix1 = []


def display_matrix(matrix):
    for val in matrix:
        print(val)
    return

for val1 in range(i):
    row = []
    for val2 in range(j):
        print("Enter M{}{} element of the matrix 1:".format(val1+1, val2+1))
        a = int(input())
        row.append(a)
    matrix1.append(row)
print("The first matrix is: ")
display_matrix(matrix1)


m = int(input("Enter no. of rows of matrix2: "))
n = int(input("Enter no. of rows of matrix2: "))
matrix2 = []


for val1 in range(m):
    row = []
    for val2 in range(n):
        print("Enter M{}{} element of the matrix 2:".format(val1 + 1, val2 + 1))
        b = int(input())
        row.append(b)
    matrix2.append(row)
print("The second matrix is: ")
display_matrix(matrix2)


def addn(matrix1, matrix2):
    add_matrix = []
    for val1 in range(i):
        rows=[]
        for val2 in range(j):
            c = matrix1[val1][val2] + matrix2[val1][val2]
            rows.append(c)
        add_matrix.append(rows)
    return add_matrix



def subn(matrix1, matrix2):
    sub_matrix = []
    for val1 in range(i):
        rows = []
        for val2 in range(j):
            c = matrix1[val1][val2] - matrix2[val1][val2]
            rows.append(c)
        sub_matrix.append(rows)
    return sub_matrix



def multn(matrix1, matrix2):
    mult_matrix = []
    for val1 in range(i):
        rows = []
        for val2 in range(n):
            counter = 0
            for val3 in range(m):
                counter += matrix1[val1][val3] * matrix2[val3][val2]
            rows.append(counter)
        mult_matrix.append(rows)
    return mult_matrix



def transpose(matrix):
    if matrix == matrix1:
        trans_matrix = []
        for val1 in range(j):
            rows = []
            for val2 in range(i):
                c = matrix[val2][val1]
                rows.append(c)
            trans_matrix.append(rows)
        return trans_matrix

    elif matrix == matrix2:
        trans_matrix = []
        for val1 in range(n):
            rows = []
            for val2 in range(m):
                c = matrix[val2][val1]
                rows.append(c)
            trans_matrix.append(rows)
        return trans_matrix

    else:
        pass


while True:
    print('''
Choice 1. Addition
Choice 2. Subtraction
Choice 3. Multiplication
Choice 4. Transpose''')
    p = int(input("Enter Choice No.: "))
    if p == 1:
        if (i, j) != (m, n):
            print("Addition not possible!")
        else:
            print("Addition of two matrices is: ")
            display_matrix(addn(matrix1, matrix2))
    elif p == 2:
        if (i, j) != (m, n):
            print("Subtraction not possible!")
        else:
            print("Subtraction of two matrices is: ")
            display_matrix(subn(matrix1, matrix2))
    elif p == 3:
        if j != m:
            print("Matrix multiplication for given matrices is not possible. ")
        else:
            print("Multiplication of two matrices is: ")
            display_matrix(multn(matrix1, matrix2))
    elif p == 4:
        print("Choice 1. Matrix 1 \nChoice 2. Matrix 2")
        q = int(input("Enter choice no. of the matrix of which the transpose is required: "))
        if q == 1:
            print("Transpose of Matrix 1 is: ")
            display_matrix(transpose(matrix1))
        elif q == 2:
            print("Transpose of Matrix 2 is: ")
            display_matrix(transpose(matrix2))
        else:
            pass
    else:
        break