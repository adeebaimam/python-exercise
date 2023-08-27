'''
The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
10th year - 10000
9th year - 9000
8th year - 8100 and so on
'''
import math
current_population=10000
print(current_population)
for years in range(1,10):
    current_population-=(0.1)*current_population 
    print(math.floor(current_population))





#else other way
import math
def population(x):
    for i in range(1,10):
        x-=(0.1)*x
        print(math.floor(x))
population(10000)
