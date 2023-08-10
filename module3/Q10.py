#Display Fibonacci series up to 10 terms
num1 = 0
num2 = 1
sum = 0
for n in range(0,10):
    sum = num1+num2 
    print(num1)
    #taking second nums as first and first nums as second
    num1=num2
    num2 = sum
    
