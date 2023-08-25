#Write  a program that will tell whether the given number is divisible by 3 & 6.
n= int(input("enter a number = "))
if n%3==0 and n%2==0:
    print('number is divisible by 6')
elif n%3==0:
    print('number is divisible  by 3')
else:
    print("number is neither divisible 3 nor 6")
