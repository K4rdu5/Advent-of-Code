#Day 1 part 1
data = open("DataDay1.txt", "r").read().split("\n")
sum = 1
i = 0
for height in data:
    if height >= data[i-1]:
        sum += 1
    i += 1
print(sum)

#Day 1 part 2
data = open("DataDay1.txt", "r").read().split("\n")
data3 = []
i=0
j=3

for d in data:
    if j == 2001:
        continue
    lst = data[i:j]
    sum = int(lst[0]) + int(lst[1]) + int(lst[2])
    data3.append(sum)
    
    i += 1
    j += 1

bigger = 0
n = 0
for height in data3:
    if height > data3[n-1]:
        bigger += 1
    n += 1
print(bigger)
