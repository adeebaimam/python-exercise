#Find the factorial of a given number
def factorial(a):
    if a==0:
        print("factorial is",a)
    elif a==1:
        return a
    else:
      #function call using recursion
        return a* factorial(a-1)

print("the factorial of 5 is", factorial(5))
