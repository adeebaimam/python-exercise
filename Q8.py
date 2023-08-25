#Write a program to find the euclidean distance between two coordinates.
import math
n1 = input("Enter first coordinates: ")
x1,y1=map(int,n1.split())
print("x1=" ,x1 ,"y1=" ,y1)
n2 = input("Enter first coordinates: ")
x2,y2=map(int,n2.split())
print("x2=" ,x2 ,"y2=" ,y2)
x=math.pow(x2-x1,2)
y=math.pow(y2-y1,2)
Euclidean_Distance=math.sqrt(x+y)


print(Euclidean_Distance)
