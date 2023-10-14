# Two numbers are input through keyboard at different location C and D.WAP to interchange the contents of C and D

#include<stdio.h>
#include<math.h>
int main()
{

int C,D,temp;
printf("Input Two Numbers C,D:  ");
scanf("%d%d",&C,&D);
temp=C;
C=D;
D=temp;
printf("After interchanging numbers C=%d ,D=%d",C,D);
return 0;
}
