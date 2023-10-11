# Peak of mountain problem i.e to find the index of greatest number


'''
appoach-to find the greatest number we use binary search techinque 
1.we will first find the middle index number.
2.Now compare that middle index number with both the left and right number.
3.If middle index number is greater than boyh lef and right number, return that mid index.
4.And if middle index number is smaller than left or right index number ,we will again find the mid after excluding them lef or right according to the list number
'''

def peak(list1):
    start=0
    end=len(list1)-1
    
    while start<=end:
        mid=(start+end)//2
        
        if list1[mid-1]< list1[mid] >list1[mid+1]:     
            return mid
        
        elif list1[mid]<list1[mid+1]:
            start=mid+1
            
        elif list1[mid]<list1[mid-1]:
            end = mid-1
            
        mid=(start+end)//2
        
    return 

list1=[24,69,100,99,79,78,67,36,26,19]    
print(peak(list1))
