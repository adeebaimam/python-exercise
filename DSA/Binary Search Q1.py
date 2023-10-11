#Binary Search code

def search(list1,key):
    
    start=0                   # starting index=0
    end=len(list1)-1          # ending index = index of last key from the list -1
    
    
    while start<=end:
        
        mid=(start+end)//2     #finding the middle term
        if key==list1[mid]:
            return mid
        
        if key>list1[mid]:
            start=mid+1
            
        elif key<list1[mid]:
            end=mid-1
            
        mid=(start+end)//2      #again modifing it
        
    return ("Not Found")

list1=[8,12,15,19,20,25]
print(search(list1,15))
    
