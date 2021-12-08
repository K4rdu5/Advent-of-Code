#Day 3 part 2

#Might come back and make more pythonic...

from collections import Counter
data = open("DataDay3.txt", "r").read().split("\n")
copy = data

for i in range(len(data[0])):
    most = Counter([p[i] for p in data]).most_common(1)[0][0]
    if most == "0":
        data = sorted([num for num in data if num[i] == most], reverse=True)
    else:
        data = sorted([num for num in data if num[i] == most], reverse=True)

o2 = data[0]
print(f"Oxygen generator rating is: {int(o2, 2)}")

for i in range(len(copy[0])):
    least = Counter([p[i] for p in copy]).most_common()[-1][0]
    if least == "0":
        copy = sorted([num for num in copy if num[i] == least], reverse=True)
    else:
        copy = sorted([num for num in copy if num[i] == least], reverse=True)

co2 = copy[0]
print(f"CO2 scrubber rating is: {int(co2, 2)}")
print(f"Life support rating is: {int(o2, 2)*int(co2, 2)}")
