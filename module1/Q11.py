#Exercise 10: Create a new list from a two list using the following condition
import random

list1 = [23,56,78,10,20]
list2 = [15,33,70,62,12]

#combine both the list 
combined_list = list1+list2

# assigning list3 to give random no.
list3 = random.choice(combined_list)

# using for loop for giving random output in given range 
for numbers in range(5):
    print(random.choice(combined_list))
