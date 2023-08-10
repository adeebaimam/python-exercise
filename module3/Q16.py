#Find the sum of the series upto n terms
#2+22+222+2222+22222
def series(n):
    sum = 0
    current_no = 2
    for i in range (n):
        sum +=current_no
        current_no=current_no*10+2
        
    return(sum)
print(series(5))
    
