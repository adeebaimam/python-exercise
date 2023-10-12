#Finding the square root using binary search taking an approximation 
'''
approach - logically suare root of any number will lie within the search space(i.e between 0 to n )
so we will do binary search on that search space and find mid 
if mid is greater than the value we will ignore the right side and again do binary search on left side 
and if mid is smaller than the value we will ignore the left side and again do binary search and both the step will continue untill square root of a number is not fount or close to sqare root of a number 
'''
def Square_root(n):
    start=0
    last=n
    store=0
    
    while start<=last:
        mid=(start+last)//2
        
        square=mid*mid
        
        if n==square:
            return mid
        if n<=square:
            
            last = mid-1
            
        else:
            store=mid
            start = mid+1
            
        mid=(start+last)//2
        
    return store
n=19
print(Square_root(n))
