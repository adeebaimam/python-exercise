#Write a program to print the first 25 odd numbers
n=int(input(" first n odd numbers: "))
count=0

for i in range(1,n*2):
    if i%2!=0:
        print(i)
        count+=1
        if count==25:
            break
