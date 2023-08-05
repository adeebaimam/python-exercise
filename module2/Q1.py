#Exercise 1A: Create a string made of the first, middle and last character
mystr = "james"
#to grt the first character
first = mystr[0]
#to get the last character
last = mystr[-1]
#for length of the string
x = len(mystr)
#get the middle endex no. with help of above code
mid = int(x/2)
#here,to get the mid character
y = mystr[mid]
#concatenation of all the acquired character
new_str = (first+y+last)
print(new_str)
