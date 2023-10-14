#include <stdio.h>
#include <math.h>

int main() {
    float L1,L2,G1,G2,D;
    // Write C code here
    printf("Enter the value of latitide in degrees(L1,L2): ");
    scanf("%f%f",&L1,&L2);
    printf("Enter the value of longitude in degrees(G1,G2):");
    scanf("%f%f",&G1,&G2);
    D = 3963*(acos(sin(L1)*sin(L2)+cos(L1)*cos(L2)*cos(G2-G1)));
    printf("Distance between latitude and longitude in nautical miles = %f",D);
    return 0;
}
