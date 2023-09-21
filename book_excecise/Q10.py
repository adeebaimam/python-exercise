#write a program to compute the aarea of a triangle and a circle by overloading the area() function.


def area(shape,*args):          
    if shape == 'triangle':
        b,h=args
        area_triangle = (b*h)/2
        return area_triangle
    elif shape == 'circle':
        r=args[0]
        area_circle=3.14*(r**2)
        return area_circle
    else:
        return None
    
    
shape=input('Enter shape : ')
if shape=='triangle':
    b=float(input('Enter base of a triangle: '))
    h=float(input('Enter height of a triangle: '))
    triangle=area(shape,b,h)
    
    print(f'Area of the triangle: {triangle:.2f}')
    
elif shape=='circle':
    r=float(input('Enter radius of a circle: '))
    circle=area(shape,r)
    
    print(f'Area of the circle: {circle:.2f}')
    
else:
    print('Invalid shape, enter either Triangle or Circle')
    
      

      
