#Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers 
list = [21,5,6,20,59,43,54,236]
list1 = []
list2 = []
for i in list:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print('list of even numbers: ',list1)
print("list of odd numbers: ",list2)
