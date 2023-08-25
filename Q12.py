#Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math
r= int(input("Radius= "))
h= int(input("Height= "))
volume = math.pi*math.pow(r,2)*h
print("volume of cylinder= ",volume)
cost = volume*40  #cost of one litre milk is =40rs
print('cost= ',cost)
