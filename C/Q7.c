//WAP to input angle and print all the Trigonometric Ratios.

#include<stdio.h>
#include<math.h>
int main()
{
printf("Enter the value of angle\n");
float angle;
scanf("%f",&angle);
float angle_radian = angle*3.14/180.0;
printf("The sine of angle = %f.\n",sin(angle_radian));
printf("The cosine of angle = %f.\n",cos(angle_radian));
printf("The tangent of angle = %f.\n",tan(angle_radian));
printf("The cotangent of angle = %f.\n",(1/(tan(angle_radian))));
printf("The cosecant of angle = %f.\n",(1/(sin(angle_radian))));
printf("The secant of angle = %f.\n",(1/(cos(angle_radian))));
return 0;
}
