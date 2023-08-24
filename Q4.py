#Write a program that will give you the sum of 3 digits
n=int(input('enter three digit number: '))
if 100<=n<=999:
    sum=0
    while n>0:
        get_no= n%10
        sum+=get_no
        n=n//10
    print(sum)
else:
    print("enter valid three digit no.")
