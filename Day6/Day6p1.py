#Day 6 part 1
datastring = open("DataDay6.txt", "r").read().split(",")
data = [int(x) for x in datastring]

for i in range(80):
    for j in range(len(data)):
        if data[j] == 0:
            data[j] = 7
            data.append(8)
        data[j] = data[j]-1
print(len(data))
