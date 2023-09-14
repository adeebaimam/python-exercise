''' An electricity board charges the following rates to domestic users to discouragelarge consump tion of energy:
For the first 100 units - 60P per unit
For next 200 units      - 80P per unit
Beyond 300 units        - 90P per unit
All users are charged a minimum of Rs. 50.00. If the total amount is more than Rs. 300.00 then an additional surcharge of 15% is added.
Write a program to read the names of users and number of units consumed and print out the charges with names.
'''


n=int(input(f'Units consumed = '))

#calculating for first 100 units as 60p per unit 
if 0<n<100:
    first=n*0.60
    print(f'Cost for {n} units = {first}')
    total_charges=50+first #here 50rs is extra charges for every user
    print(f'Total charges for {n} units = {total_charges}')
    
#calculating for next 200 units as 80p per unit
elif 0<n<300:
    
    #total units - 100 for calculating next 200 units
    x=n-100        
    second=100*0.60+x*0.80
    print(f'Cost for {n} units = {second}')
    total_charges=50+second  #here 50rs is extra charges for every user
    print(f'Total charges for {n} units = {total_charges}')
    
    
#calculating beyond 300 units as 90p per unit
elif n>300:
    
    #total unit -(first 100 units -200 unit)
    x=n-300
    third=100*0.60+200*0.80+x*0.90
    print(f'Cost for {n} units = {third}')
    total_charges=50+third    #here 50rs is extra charges for every user
    print(f'Total charges for {n} units = {total_charges}')
    
    
#if total amount is more than 300rs additional charge of 15% is added
if total_charges>300:
    Exceeded_amount=total_charges+(0.15*total_charges)
    print(f'Total charges is more than 300Rs, so the exceeded amount is = {Exceeded_amount}')
