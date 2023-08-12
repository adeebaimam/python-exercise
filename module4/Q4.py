Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def calculate(a):
    if a==0:
        return 0
    elif a==1:
        return a
    else:
        return a+calculate(a-1)
calculate(10)
