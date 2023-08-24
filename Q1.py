#User will input (3ages).Find the oldest one
n1=input("enter  Rahul's age ")
n2=input("enter Rohan's age ")
n3=input("enter Monika's age ")
if n1>n2 and n1>n3:
    print("Rahul is oldest of all")
elif n2>n1 and n2>n3:
    print("Rohan is oldest of all")
else:
    print("Monika is oldest of all")
