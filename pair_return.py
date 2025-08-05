matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

num=int(input("Enter a number you want to search: "))

pair=(-1,-1)
for i in range(3):
    for j in range (3):
        if matrix[i][j] == num:
            pair=(i+1,j+1)
            break
        
print(">>>>>>>>>>> Index Pair <<<<<<<<<<")
print(pair)