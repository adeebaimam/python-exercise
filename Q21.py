#Write a program that can multiply 2 numbers provided by the user without using the * operator
n=input("enter two numbers: ")
n1,n2=map(int,n.split())
print('n1 =', n1, 'n2 =', n2)
sum=0
for i in range(0,n2):
    sum+=n1
print(sum)
    
