#Calculate the angle between the hour hand and minute hand.; we need to print a minimum of two. Also, we need to print the floor of the final result angle
import math
h=int(input("enter the hour: "))
m=int(input("enter the minute: "))
Angle_min=6*m  #for each min-60 degree
Angle_hour=30*h+0.5*m 
if Angle_min>Angle_hour:
    Angle_between_them=Angle_min-Angle_hour
else:
    Angle_between_them=Angle_hour-Angle_min
print("Angle_between_them ",Angle_between_them)
floor_value=math.floor(Angle_between_them)
print("floor_value ",floor_value)
