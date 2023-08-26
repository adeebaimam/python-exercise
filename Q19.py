#write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).
n=int(input("Enter salary: "))
deduction = n-((10/100)*n+(5/100)*n+(3/100)*n) #HRA(10%),DA(5%),PF(3%)
if 500000<=n<=1000000:
    salary = deduction-(10/100)*deduction
    print("salary",salary)
elif 1100000<=n<=2000000:
    salary = deduction-(20/100)*deduction
    print("salary",salary)
elif n>2000000:
    salary = deduction-(30/100)*deduction
    print("salary",salary)
elif 0<n<=100000:
    print("k")
