#Exercise 6: Count the total number of digits in a number
n = int(input())
count = 0
while n != 0:
    n = n // 10
    count += 1
print(count)
