#Write a program that can find the factorial of a given number provided by the user.
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return(n*factorial(n-1))
factorial(4)
