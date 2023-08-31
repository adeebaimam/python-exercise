##Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
import math
a = int(input('nemo '))
b = int(input('deno '))

original_fraction=f'{a}/{b}'
gcd = math.gcd(a,b)
simplified_numerator = a//gcd
simplified_denominator = b//gcd
simplified_fraction=(f'{simplified_numerator}/{simplified_denominator}')
print('original_fraction',original_fraction)
print('gcd',gcd)
print('simplified_fraction',simplified_fraction)
