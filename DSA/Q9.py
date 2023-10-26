#Painters partition problem using binary search.This problem involves partition of n number of boards of any length to be painted  by 'painters' painters while minimizing the maximum number of boards any painter has to paint.

def isPartitionPossible(arr,n,painters,mid):
    painter_count=1
    paint_board=0
    
    for i in range(n):
        
        if paint_board + arr[i] <= mid:
            paint_board += arr[i]
            
        else:
            painter_count += 1
            
            if painter_count > painters:
                return False
                
            paint_board=arr[i]
            
    return  True


def painter_partition(arr,n,painters):
    start=0
    end=sum(arr)
    ans=-1
    
    while start<=end:
        mid = start + (end-start) //2
        
        if isPartitionPossible(arr,n,painters,mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1
            
        mid = start + (end-start) //2
        
    return ans

arr=[5,10,30,20,15]
n=5
painters=3
print(painter_partition(arr,n,painters))
