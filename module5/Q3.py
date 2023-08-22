#Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count={}
for i in sample_list:
    if i in count:
        count[i]+=1
    else :
        count[i]=1
print(count)
