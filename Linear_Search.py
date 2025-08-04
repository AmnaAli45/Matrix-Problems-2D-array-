#Creating a matrix
rows=int(input("Enter the number of rows of a matrix: "))
cols=int(input("Enter the number of columns of a matrix: "))

matrix=[]

for i in range (rows):
    row=[]
    for j in range (cols):
        value = eval(input(f"Enter the value for {i+1} row and {j+1} col: "))
        row.append(value)
    matrix.append(row)

print("-----------------Matrix-----------------")
print(matrix)

#Applying linear search algorithm
print("-----------------Linear Search-----------------")

num=eval(input("Enter the number you want to search from matrix: "))
found = False
for i in range (rows):
    for j in range (cols):
        if matrix[i][j] == num:
            found = True

if found:
    print ("number is found")
else:
    print ("number not found")
