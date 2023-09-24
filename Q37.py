#Wap to input numbers and find the runner up from given n input numbers

n=int(input())
arr=list(map(int,input().split()))
sorted_number=list(sorted(arr))
unique=[]
for i in sorted_number:
    if i not in unique:
        unique.append(i)
print(unique[-2])
