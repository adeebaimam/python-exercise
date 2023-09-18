#write a program to read a matrix of size m x n from the keyboard and display the same on the the screen using functions

def matrix_(m,n):
    matrix=[]
    for i in range(m):
        row=[]
        for j in range(n):
            k=int(input())
            row.append(k)
        matrix.append(row)
    return matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)

#to input rows and columns        
m=int(input('Enter number of rows: '))
n=int(input('Enter number of columns: '))

#to read the matrix
matrix=matrix_(m,n)

#display the matrix
display_matrix(matrix)
