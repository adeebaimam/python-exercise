#Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

#narcisstist are special case of larger numbers called armstrong number
n=int(input("Enter four digit numbers: "))

if 1000<=n<=9999:
    count=0
    original_num=n
    while n>0:
        n=n//10
        count+=1
    n=original_num
    sum=0
    while n>0:
        get_num=n%10
        power_num=pow(get_num,count)
        sum+=power_num
        n=n//10
    if sum==original_num:
        print(original_num, "Is a narcissist number ")
    else:
        print('Is not a narcissist number ')
else:
    print("invalid number,enter 4 digit number ")
