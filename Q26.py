#Write a program to find the compound interest 
P = float(input("Principal: "))
r = float(input("Rate: "))
n = float(input("num of times compounded per year: "))
t = float(input("Time: "))
power = n*t

C=float(P*(1+r/(n*100))**power)
print("Compound Interest: ",C)
