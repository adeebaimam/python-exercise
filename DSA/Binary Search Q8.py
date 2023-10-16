#Book allocation problem using binary search.This problem involves allocating books to 'student' students while minimizing the maximum number of pages any student has to read.


def isAlocationPossible(arr,n,student,mid):
    studentCount=1
    pageSum=0
    
    for i in range(n):
        if pageSum + arr[i] <= mid:
            pageSum += arr[i]
            
        else:
            studentCount += 1
            
            if studentCount>student:
                return False
              
            pageSum=arr[i]
            
    return True


def book_allocation(arr,n,student):
    start=max(arr)
    end=sum(arr)
    ans=-1
    
    while start <= end:
        mid = start + (end-start)//2
        
        if isAlocationPossible(arr,n,student,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
            
        mid=start+(end-start)//2
        
    return ans

arr=[12,34,67,90]
n=4
student=2
print(book_allocation(arr,n,student))
