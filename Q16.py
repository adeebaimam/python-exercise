#Write a program that will take three digits from the user and add the square of each digit.
n=int(input('Enter three digit number: '))
if 100<=n<=999:
    sum=0
    while n>0:
        get_num=n%10
        square=get_num**2
        sum+=square
        n=n//10
    print(sum)
        
