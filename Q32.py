#Write a Python Program to Find the Sum of the Series till the nth term: 
#1 + x^2/2 + x^3/3 + … x^n/n
#n will be provided by the user
import math
n = int(input('enter value of n: '))
x = int(input("enter value of x: "))
result = 1

for i in range(2,n+1):
    square = pow(x,i)
    result = result + (square/i)                                                             
print(result)
    
