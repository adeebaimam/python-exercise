'''
Exercise 12: Calculate income tax for the given income by adhering to the below rules.
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
'''
income = 45000
tax_to_pay = 0
print('income', income)

#for 1st 10000
if income <= 10000:
    tax_to_pay = 0
elif income <= 20000:
    #no tax for first 10000 
    x = income - 10000
    tax_to_pay = x*(10/100)
else:
    #for 1st 10000
    tax_to_pay = 0
    #for 2nd 10000
    tax_to_pay = 10000*(10/100)
    #for remaining
    y = income - 20000
    tax_to_pay += y*(20/100)
print('tax = ',tax_to_pay)    
    
