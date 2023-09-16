# The natural logarithm can be approximated by the following series.
#((x-1)/x)+1/2((x-1)/x)^2+1/2((x-1)/x)^3+...
#If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.
x = int(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
result = 1-1/x
for i in range(2,n+1):
    series = pow(((x-1)/x),i)
    result = result + (series/2)
print(result)
