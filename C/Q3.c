/* WAP to input five digit number from the keyboard and calculate the sum of its digit*/

#include <stdio.h>

int main() {
    int n,r,sum=0;
    
    printf("Enter the five digit number: ");
    scanf("%d",&n);
    while (n>0)
    {
        r=n%10;
        sum+=r;
        n=n/10;
    }
    
    printf("The sum of digits is = %d",sum);
    
    return 0;
}
