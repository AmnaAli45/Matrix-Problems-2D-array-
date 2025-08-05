rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

matrix=[]

for i in range (rows):
    row=[]
    for j in range (cols):
        value = eval(input("Enter the value: "))
        row.append(value)
    matrix.append(row)

sum=[]
for i in range (rows):
    add=0
    for j in range (cols):
        add += matrix[i][j]
    sum.append(add)

max_sum=max(sum)
print(f"MAximum Row Sum is: {max_sum}")
