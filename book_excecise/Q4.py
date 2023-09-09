#Write programs to evaluate the following functions to 0.0001% accuracy.
#(a) sin x = x - ((x^3)/(3!)) + ((x^5)/(5!)) - ((x^7)/(7!)) + ...

x = float(input('Enter the value of x in radians: '))
n = int(input('Enter the number of terms: '))

# Initialize variables
sin_x = 0
term = x
sign = 1

for i in range(1, n + 1):
    sin_x += term
    sign *= -1
    term *= (x * x) / ((2 * i) * (2 * i + 1))

print(f"Approximation of sin({x}) with {n} terms: {sin_x:.6f}")
