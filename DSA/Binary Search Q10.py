#Aggressive cow . In this problem, you're given a set of stalls and a set of cows, and you need to find the maximum distance such that each cow can be placed in a stall, with the constraint that the cows should be placed as far apart as possible.

def isSeparatingPossible(stall,n,cows,mid):
    cowCount=1
    stallCount=0
    
    for i in range(n):
        if stall[i]-stallCount>=mid:
            cowCount += 1
            
            if cowCount==cows:
                return True
            stallCount = stall[i]
    return False
        
    
def aggressive_cow(stall,n,cows):
    stall.sort()
    
    start=0
    end = stall[-1]-stall[0]
    ans=-1
    
    while start<=end:
        mid=start + (end-start) //2
        
        if isSeparatingPossible(stall,n,cows,mid):
            ans = mid
            start=mid+1
        else:
            end = mid-1
            
        mid=start + (end-start) //2
        
    return ans
stall=[4,1,2,3,6]
n=5
cows=2
print(aggressive_cow(stall,n,cows))
