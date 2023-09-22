#Write a function power() to raise a number m to a power n. The function takes a double value for m and int value for n, and returns the result correctly. Use a default value of 2 for n to make the function to calculate squares when this argument is omitted. Write a main that gets the values of m and n from the user to test the function

#function to raise a number m to n
def power(m,n=2):      #taking 2 as a default value for n
    result=pow(m,n)        
    return result

m=float(input("Value of m: "))

try:                               #using hit and except method to get error free answer by
    n=int(input("Value of n: "))   #entering enter key without taking any input for n 
except ValueError:
    n=2

result=power(m,n)
print(f'{m} raise to power {n} = {result}')
