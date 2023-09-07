'''Write a program to evaluate the following investment equation
            V = P (1 + r)^n
and print the tables which would give the value of V for various combination of the following values of P, r and n:
       P: 1000, 2000, 3000, ...., 10,000
       r: 0.10, 0.11, 0.12, ...., 0.20
       n: 1, 2, 3, ...., 10

Hint: P is the principal amount and V is the value of money at the end of n years. This equation can be recursively written as
       V = P (1 + r)
       P = V
In other words, the value of money at the end of the first year becomes the principal amount for the next year, and so on
'''

Principal=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
rate=[0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19]
time=[1,2,3,4,5,6,7,8,9,10]
#for header of a table 
print("P\t\tr\t\tn\t\tV")
for P in Principal:
    for r in rate:
        for t in time:
            #calculating value using formula
            V=P*(1+r)**t
            print(f'{P}\t\t{r:.2f}\t\t{t}\t\t{V:.2f}')
