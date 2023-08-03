#Exercise 9: Check Palindrome Number

#take input
n = int(input("enter a no. "))
print( "actual_no. = ", n)

reverse = 0    
while n > 0:
    digit = n%10
    reverse = reverse*10 + digit           
    n = n//10 
print("reversed no. = ", reverse )
    
if reverse == n:
    print(" yes, it is a palindrome no")
else:
    print( "no, it is not a plainfrome no.")
        
