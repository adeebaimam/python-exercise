//Wind chill factor is the felt air temperature on exposed skin due to wind .WAP to recieve values of t and v and calculate wind-chill factor  

#include <stdio.h>
#include <math.h>

int main() {
    float t,v,wcf;
    // Write C code here
    printf("Enter the value of temperature(t) in Fahrenheit and wind velocity(v) in mph: ");
    scanf("%f%f",&t,&v);
    wcf = 35.74+0.6215*t+(0.4275*t-35.75)*pow(v,0.16);
    printf("Wind chill factor at given values =%f F",wcf);
    return 0;
}
