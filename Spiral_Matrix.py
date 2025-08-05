matrix= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# no. of rows
m = len(matrix)

# no. of columns
n = len(matrix[0])

spriral=[]

srow = 0
erow = m-1
scol = 0
ecol = n-1

while(srow <= erow and scol <= ecol):
    # Top Boundary
    for j in range (scol,ecol + 1):
        spriral.append(matrix[srow][j])
    
    # Right Boundary
    for i in range (srow+1,erow+1):
        spriral.append(matrix[i][ecol])
    
    #Bottom Boundary
    for j in range (ecol-1,scol-1,-1):
        spriral.append(matrix[erow][j])
    
    #Left Boundary
    for i in range (erow-1,srow,-1):
        spriral.append(matrix[i][srow])
    
    srow +=1
    erow -= 1
    scol += 1
    ecol -= 1

print(spriral)