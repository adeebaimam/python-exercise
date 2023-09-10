#Write programs to evaluate the following functions to 0.0001% accuracy.
#(a) sin x = x - ((x^3)/(3!)) + ((x^5)/(5!)) - ((x^7)/(7!)) + ...

# function to find factorial of a number
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n *factorial(n-1)
    
# function to calculate taylor series od sinx
def taylor_series(x,n_terms):
    
    result = 0
    
    for i in range(n_terms):
        sign = (-1)**i    # to change sign after each term 
        
        #to calculate each term and storing them into result
        term= pow(x,2*i+1)/factorial(2*i+1)   
        result +=sign*term
        
    return result

x = float(input('Enter the value of x: '))

# to convert degree into radian
radian = x*3.14/180
print(f'sin{x} = {radian} rad')

n_terms = int(input('Enter the number od terms to use in taylors series: '))

approximation = taylor_series(radian,n_terms)
print(f'Approximation of sin({x}) to {n_terms} terms: {approximation:.6f}')
