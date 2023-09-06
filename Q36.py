#Write a python program to remove all the duplicates from a list
n=[4,5,21,5,67,89,0,21]
c=[]
for i in n:
    if i not in c:
        c.append(i)
print(c)
