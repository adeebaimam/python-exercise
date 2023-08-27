#Print all the armstrong numbers in the range of 100 to 1000
import math

for n in range(100,1000):
    sum=0
    original_no=n
    while n>0:
        get_num=n%10
        power_num=pow(get_num,3)
        sum+=power_num
        n=n//10
        
    if original_no==sum: 
            
        print(original_no)
        
