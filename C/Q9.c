//WAP to obtain reversed number and to determine whether the original and reversed numbers are equal or not

#include <stdio.h>

int main() {
    int originalNumber,reversedNumber=0,r;
    // Write C code here
    printf("Enter five digit number: ");
    scanf("%d",&originalNumber);
    while (originalNumber>0)
    {
        r=originalNumber%10;
        reversedNumber = reversedNumber*10+r;
        originalNumber = originalNumber/10;
    }
    printf("Reversed number is = %d ",reversedNumber);
    
    if (originalNumber=reversedNumber)
    {
        printf("\noriginal number is equal to reversed number");
    }
    else
    {
        printf("original number is not equal to reversed number");
    }
    return 0;
}
