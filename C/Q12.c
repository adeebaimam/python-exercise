//WAP to find the area and perimeter of rectangle and compare them

#include <stdio.h>

int main() {
    int l,b,a,p;
    // Write C code here
    scanf("%d%d",&l,&b);
    printf("Length = %d\nBreadth = %d",l,b);
    
    a = l*b;
    p = 2*(l+b);
    
    printf("\nArea of rectangle = %d\nPerimeter of rectangle = %d",a,p);
    
    if (a>p)
    {
        printf("\nArea of the rectangle is greater than its perimeter");
    }
    else 
    {
        printf("\nArea of the rectangle is less than its perimeter");
    }
    
    return 0;
}
