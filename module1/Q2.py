#Exercise 2: Print the sum of the current number and the previous number
previous_num=0
for i in range(0,10):
    no_sum = previous_num+i
    print("current num",i,"previous num",previous_num,"sum of both no.s",no_sum)
    
    previous_num =i

