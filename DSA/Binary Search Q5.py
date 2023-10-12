#Pivot of an array i.e smallest element of an array
'''approach-campare each mid element with the 1st index element of an array
if mid index element is greater than 1st index element than shift the mid point towards right
if the mid index element is less than 1st index elemet  than return mid 
'''

def pivot(arr):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]>= arr[0]:   
            start=mid+1
            
        else:
            return mid
        mid=(start+end)//2
        
    return    

arr=[7,9,1,2,3]
pivot(arr)
