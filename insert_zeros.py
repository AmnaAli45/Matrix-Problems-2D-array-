# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place

r= int (input("Enter the number of rows: "))
c= int (input("Enter the number of columns: "))

for i in range (r):
    for j in range (c):
        value = int(input("Enter the value: "))
        