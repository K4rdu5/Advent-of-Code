data = open("DataDay3.txt", "r").read().split("\n")
gamma = []
epsilon = []

for i in range(len(data[0])):
    pos = [p[i] for p in data]
    gamma.append("0" if pos.count("0") > pos.count("1") else "1")
    epsilon.append("1" if pos.count("0") > pos.count("1") else "0")

gamma = "".join(str(g) for g in gamma)
epsilon = "".join(str(e) for e in epsilon)

print(f"Power consumption is: {int(gamma, 2) * int(epsilon, 2)}")
