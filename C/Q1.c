//WAp to covert fahrenheit into centigrade

#include <stdio.h>

int main() {
    float F,C;
    // Write C code here
    printf("Enter the temperature in Fahrenheit: ");
    scanf("%f",&F);
    C=(F-32)*5/9;
    printf("Temperature into Centrigrade degree =%f",C);
    return 0;
}
