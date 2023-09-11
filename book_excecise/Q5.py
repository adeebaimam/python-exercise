#SUM = 1 + ((1/2)^2) + ((1/3)^3) + ((1/4)^4) + ...

n=int(input('Enter the number of terms till whose some is to be evaluated'))
result=0
for i in range(1,n+1):
    
    ##to calculate the current term
    x= (1/i)**i
    print(f'Term {i} st series is: {x}')
    
    #to calculate repeating sum upto ith term
    result +=x
    
    print(f'sum of {i} st term is: {result:.6f}')
    
#calculate sum of total term
print(f'Total Sum of {n} terms upto given approximation is :{result:.6f}')
    
    
