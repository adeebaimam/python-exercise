#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
n=int(input('enter four digit number '))
if 1000<=n<=9999:
    reverse=0
    while n>0:
        get_no=n%10
        reverse=reverse*10+get_no
        n=n//10
    print(reverse)
else:
    print("enter valid 4 digit no.")
