#wap to calculate the batting average of given inputs in a complete tabular form including the average column

Players_name=['Sachin','Saurav','Rahul']
Runs=[8430,4200,3350]
Innings=[230,130,105]
Times_not_out=[18,9,11]

print('P\t\tR\t\tI\t\tT\t\tAvg')

for p,r,i,t in zip(Players_name,Runs,Innings,Times_not_out):   
    
    avg=r/(i-t)     #calculating batting average ,runs scored /innings-times_out
        
    print(f'{p}\t\t{r}\t\t{i}\t\t{t}\t\t{avg:.2f}')
