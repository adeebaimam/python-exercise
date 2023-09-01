#Count the number of vowels in a string provided by the user.
vowels = ['a','e','i','o','u']
n = input('enter any string: ')
count=0
for i in n:
    if i in vowels:
        count+=1
print(count)
        
