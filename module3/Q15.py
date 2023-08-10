#Calculate the cube of all numbers from 1 to a given number
n = int(input())
for i in range(1,n+1):
    cube = i**3
    print("Current number is ",i,"and the cube is", cube)
