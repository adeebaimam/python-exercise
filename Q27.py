#Take a number from the user and find the number of digits in it. 
n = int(input("enter the number: "))
count=0
while n>0:
    n=n//10
    count+=1
print(f'number of digits is {count}')
