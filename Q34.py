# Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
sum = 0
count = 0
while (True):
    print("enter your number: ")
    n = int(input())
    if n != 0:
        sum +=n
        count+=1
        continue
    else:
        break
print("sum of all non-zero numbers: ",sum) 
print("count of all numbers: ", count)
average = (sum/count)
print("average of all number: ",average)
