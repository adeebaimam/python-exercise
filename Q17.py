#Write a program that will check whether the number is armstrong number or not.
import math
n= int(input("Enter a number: "))
original_value=n
count=0
while n>0:
    n=n//10
    count+=1
    
n=original_value
sum=0
while n>0:
    get_num = n%10
    power_num=pow(get_num,count)
    sum+=power_num
    n=n//10  
if sum == original_value:
    print(original_value,"is an armstrong num.")
else:
    print(original_value,"is not an armstrong num.")

    
