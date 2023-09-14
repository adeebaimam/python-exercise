'''Write a program to calculate variance and standard deviation of N numbers
                 N    _
    Variance=1/N.∑(xi-x)^2
                 i-1
                 
                           N    _
    Standard Variance=[1/N.∑(xi-x)^2]^1/2
                           i-1
    
'''                        

import math
# Here N is  total number of datapoints
N=list(map(int,input("Enter yor data_points: ").split()))

sum=0
count=0
s_sum=0

# Function to calculate mean by formula = total sum of all numbers/total numbers
for i in N:
    count+=1   # calculating total no. in data_points i.e N
    sum+=i     # calculating total sum of N numbers
X_=sum/count   #here X_ is mean of N numbers
print(f'Mean of {N} is {sum}/{count} = {X_:.2f}')
      
for i in N:
    x=(i-X_)**2   #calculating (xi-X_)^2
    s_sum+=x      # And summing them up
    
    print(f'For {i}--> {i}-{X_:.2f} = {x:.2f}')
    
Var=s_sum/count    # Calculating variance =(xi-X_)^2/N, here X_ is mean of N numbers
print(f'Sum of squared difference = {s_sum:.2f}')    
print(f'Variance = {Var:.2f}')



#to calculate standard deviation 
St_Var=math.sqrt(Var)
print(f'Standard Variance = {St_Var:.2f}')
