# Generate a Python list of all the even numbers between 4 to 30
def even_no(a,b):
    even_list=[]
    for i in range(a,b):
        if i%2==0:
            even_list.append(i)
    return even_list             
        
even_no(4,30)        
