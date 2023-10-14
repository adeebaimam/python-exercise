//WAP to convert Cartesian co ordinates into polar co ordinates(r,theta) 

#include <stdio.h>
#include <conio.h>
#include <math.h>

int main() {
    float theta,x,y,r;
    // Write C code here
    printf("Enter the coordinates: ");
    scanf("%f%f",&x,&y);
    r=sqrt(x*x+y*y);
    theta=atan(y/x);
    printf("Converting cartesian co-ordinates into polar co-ordinates =(%.2f ,%.2f)",r,theta);
    return 0;
}
