#Exercise 6: Display numbers divisible by 5 from a list
number = input("enter the numbers: ").split()
number = [int(num) for num in number]
print(number)
for num in number:
    if num%5 == 0:
        print(num)
