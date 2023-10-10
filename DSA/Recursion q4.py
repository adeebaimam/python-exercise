#Saydigit--- to find number name of each digit in an integer 

arr = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
       
def func(n):
    if n==0:
        return
    else:
        digit=n%10          #extracting last digit of a number
        n=n//10
        
        func(n)
        print(arr[digit],end=' ')    #arr[digit]= extracting the words of each digit passing in an array
func(432)
