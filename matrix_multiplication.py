# Write a program to perform matrix multiplication for two given matrices.
matrix_1 = []
matrix_2 = []

row1=int(input("Enter the no. of rows for matrix 1 : "))
col1=int(input("Enter the no. of columns for matrix 1 : "))

for i in  range (row1):
    row = []
    for j in range (col1):
        value = int(input("Enter the value for matrix_1: "))
        row.append(value)
    matrix_1.append(row)

row2=int(input("Enter the no. of rows for matrix 2 : "))
col2=int(input("Enter the no. of columns for matrix 2 : "))

for i in  range (row2):
    row = []
    for j in range (col2):
        value = int(input("Enter the value for matrix_2: "))
        row.append(value)
    matrix_2.append(row)

res = []
if col1 != row2:
    print ("Not compatible for matrix multiplication")
else:
    for i in range (row1):
        row = []
        for j in range (col2):
            value = 0
            for k in range (col1):
                value += matrix_1[i][k] * matrix_2[k][j]
            row.append(value)
        res.append(row)

print ("............ Matrix_1 ...............")
print(matrix_1)
print ("............ Matrix_2 ...............")
print(matrix_2)
print ("............ Matrix_1 X  Matrix_2 ...............")
print(res)       

