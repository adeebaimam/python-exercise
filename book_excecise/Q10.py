#write a program to compute the aarea of a triangle and a circle by overloading the area() function.
def area_triangle(b,h):
    area=(b*h)/2
    return area
def area_circle(r):
    area=3.14*(r**2)
    return area

b=float(input('Enter base of a triangle: '))
h=float(input('Enter height of a triangle: '))

triangle=area_triangle(b,h)
print(f'Area of a triangle is = {triangle:.2f}')

r=float(input('Enter radius of a circle: '))

circle=area_circle(r)
print(f'Area of a circle is = {circle:.2f}')
      
