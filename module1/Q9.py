'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
n = int(input())
# for rows
for i in range (n):
    # for columns , as each j will repeat i times
    for j in range (i):
        
    
        print( i ,end = " ")
    print("\n")
    
