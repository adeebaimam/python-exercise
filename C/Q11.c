//WAP to check to input angles of a triangle and check whether it is a valid triangkle or not 

#include <stdio.h>

int main() {
    int a1,a2,a3;
    // Write C code here
    
    scanf("%d%d%d",&a1,&a2,&a3);
    printf("First Angle  = %d\nSecond Angle = %d\nThird Angle = %d",a1,a2,a3);
    if (a1+a2+a3==180)
    {
        printf("\nThis is a valid Triangle");
    }
    else 
    {
        printf("\nThis is not a valid Triangle, TRY AGAIN");
    }
    return 0;
}
