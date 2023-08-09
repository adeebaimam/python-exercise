#Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
for num in range(start,end+1):
    #all prime numbers are greater than 1
    if num>1:
        #excluding 1
        for i in range(2,num):
            if(num%i == 0):
                #not a prime number 
                #look for next number
                break
        else:    
            print(num)
