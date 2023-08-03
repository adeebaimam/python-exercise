Exercise 5: Check if the first and last number of a list is the same
def number_check(numberlist):
    print("numbers are",numberlist)
    first_number = numberlist[0]
    last_number = numberlist[-1]
    
    if first_number == last_number:
        return True
    else:
        return False
#get input from the user and set it as a list    
numberlist = input("enter numbers").split()
#to convert the list of string into integer
numberlist = [int(num) for num in numberlist]
#call the number 
print(number_check(numberlist))
    
