//WAP to input ages of three and find the youngest of all

#include <stdio.h>

int main() {
    int r,s,a;
    // Write C code here
    
    scanf("%d%d%d",&r,&s,&a);
    printf("Age of Ram = %d\nAge of Shyam =%d\nAge of Ajay =%d",r,s,a);
    if (r<s && r<a)
    {
        printf("\nRam is youngest of all");
    }
    else if (s<r && s<a)
    {
        printf("\nShyam is youngest of all");
    }
    else
    {
        printf("\nAjay is youngest of all");
    }
        
    return 0;
}
