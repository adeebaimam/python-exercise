//WAP to calculate perimeter and circumference of a rectangle and circle

#include <stdio.h>

int main() {
    int l,b,r,p;
    float c;
    printf("Enter length and breadth of a rectangle: ");
    scanf("%d%d",&l,&b);
    p=2*(l+b);
    printf("Perimeter of a rectangle =%d",p);
    
    printf("\nEnter radius of a circle: ");
    scanf("%d",&r);
    c=2*3.14*r;
    printf("Circumference of a circle =%f",c);
    return 0;
}
