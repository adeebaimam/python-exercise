'''
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
'''
n = int(input("enter the no: "))
for i in range(n): 
    
    for j in range (i , n):
        print('*',end = " " )
    print("\n")   
    
