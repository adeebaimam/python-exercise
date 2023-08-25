#Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
n = input("enter three angles: " )
x,y,z = map(int,n.split())
if x+y+z==180:
    print("It form a triangle")
else:
    print("Does not form a triangle")
