'''
draw the pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
n = int(input("enter the no."))
#i starting from n and decreases one by one 
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("\n")
