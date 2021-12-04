#Day 2 part 1
data = open("DataDay2.txt", "r").read().split("\n")
horizontal = 0
depth = 0

for d in data:
    if "forward" in d:
        datafor = d.split("forward ")
        horizontal = horizontal + int(datafor[1])
    if "up" in d:
        dataup = d.split("up ")
        depth = depth - int(dataup[1])
    if "down" in d:
        datadown = d.split("down ")
        depth = depth + int(datadown[1])

print(horizontal * depth)

#Day 2 part 2
data = open("DataDay2.txt", "r").read().split("\n")
horizontal = 0
depth = 0
aim = 0

for d in data:
    if "forward" in d:
        datafor = d.split("forward ")
        horizontal = horizontal + int(datafor[1])
        depth = depth + int(datafor[1]) * aim
        
    if "up" in d:
        dataup = d.split("up ")
        aim = aim - int(dataup[1])
        
    if "down" in d:
        datadown = d.split("down ")
        aim = aim + int(datadown[1])
        
print(horizontal * depth)
