#Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size
new_list = []

for i in range(0, 3):
    x = sample_list[start:end]
    x.reverse()
    new_list.append(x)
    start = end
    end += chunk_size

print(new_list)
