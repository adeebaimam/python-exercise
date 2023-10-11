#find the first and the last occurrence of an element
def first_and_last_occ(list1,key):
    
    def first_occ(list1,key):

        start=0
        end=len(list1)-1
        first=0


        while start<=end:

            mid=(start+end)//2
            if key==list1[mid]:
                first=mid
                end=mid-1

            if key>list1[mid]:    #towards right
                start=mid+1

            elif key< list1[mid]:  #towards left
                end=mid-1

            mid=(start+end)//2

        return first

    def last_occ(list1,key):

        start=0
        end=len(list1)-1
        last=0

        while start<=end:

            mid=(start+end)//2
            if key==list1[mid]:
                last=mid
                start=mid+1

            if key>list1[mid]:    #towards right
                start=mid+1

            elif key< list1[mid]:  #towards left
                end=mid-1

            mid=(start+end)//2

        return last
    
    first=first_occ(list1,key)
    last=last_occ(list1,key)
    
    return first,last

list1=[2,3,3,4,4,4,5,5,5]
key=4
first_occ,last_occ=first_and_last_occ(list1,key)
print(f'first and last occurrence of {key} is at index {first_and_last_occ(list1,key)}')

