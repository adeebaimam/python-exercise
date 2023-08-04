#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base,exp):
    print("base =",base)
    print("exp =",exp)
    number = base**exp
    print(base,"raise to power",exp,"is =",number)
exponent(5,3)
