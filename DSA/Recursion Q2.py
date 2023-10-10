#fibonacchi series using recursion

#toi find nth term = sum of last 2nd and 3rd term 
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1     
    else:
        return fibo(n-1)+fibo(n-2)    #n-1 for last 2nd term and (n-2) for last 3rd term
fibo(10)   
