rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

matrix=[]

for i in range (rows):
    row=[]
    for j in range (cols):
        value = eval(input("Enter the value: "))
        row.append(value)
    matrix.append(row)


diag_sum = 0

for i in range (rows):
    for j in range (cols):
        if i ==j :
            diag_sum += matrix[i][j]

print(f"Diagonal Sum is: {diag_sum}")
