#to find an element from rotated array

def find(arr,key):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==key:
            return mid
        
        if arr[start]<=arr[mid]:              #left side
            if arr[start]<=key<arr[mid]:         #left
                end=mid-1
            else:                               #right
                start=mid+1            
                
                
        else:                               #right side
            
            if arr[mid]<key<=arr[end]:            #left
                start=mid+1
            else:                                #right
                end=mid-1
    return -1

arr=[7,9,10,15,3,5,8,17]
key=5
if find(arr,key) !=-1:
    print(f'Element {key} found at index {find(arr,key)}')
else:
    print(f'Element {key} not found')
