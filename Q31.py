#Write a program to calculate the sum of the following series till the nth term
#1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
#n will be provided by the user
class Series:
    def factorial(self,num):
        if num==1 or num==0:
            return 1
        else:
            return num*self.factorial(num-1)
    def sum_series(self,n):
        sum = 0
        for i in range(1,n+1):
            sum +=i/self.factorial(i)
        return sum
n = int(input("enter the value of n: "))
series_num = Series()
result = series_num.sum_series(n)
print(f'the sum of the series until {n} term is: ', result)
        





#other method
n = int(input('enter your number: '))
fact = 1
result = 0

for i in range(1,n+1):
    fact = fact*i
    result = result +(i/fact)
print(result)
