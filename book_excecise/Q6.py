#cosx=1-((x^2)/2!)+((x^4)/4!)-((x^6)/6!)+----

#function to calculate factorial--
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
    
#function to calculate taylor series for cosx--
def cosx_series(x,n_term):
    result=0
    
    for i in range(n_term):
        sign=(-1)**i           #for changing sign for alternating terms
        term=(x**(2*i))/factorial(2*i)
        result+=sign*term
    return result

x=float(input("Enter the value of x: "))

radian=x*3.14/180             #changing degree into radian
print(f'Value of cos({x}) into radian is:{radian}')

n_term=int(input('Enter the number of terms: '))

cosx_series(radian,n_term)
print(f'Cos({x}) series for {n_term} term is:{cosx_series(radian,n_term):.6f}')
