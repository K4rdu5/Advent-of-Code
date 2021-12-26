#Day 8 part 2
with open("DataDay8.txt", "r") as f:
    lines = f.readlines()
    data = []
    for line in lines:
        inp = sorted(["".join(sorted(x)) for x in line.strip("\n").split("|")[0].split()], key=len)
        outp = ["".join(sorted(x)) for x in line.strip("\n").split("|")[1].split()]
        data.append([inp, outp])

def diff(x,y):
    return "".join(set(x).intersection(set(y)))

gtot = 0
for cypher in data:
    #get easy nums
    c = cypher[0]
    key = dict({c[0]:1, c[1]:7, c[2]:4, c[9]:8})
    fives = [c[3], c[4], c[5]]
    sixes = [c[6], c[7], c[8]]
    #get 6
    for index in range(len(sixes)):
        if len(diff(c[0], sixes[index])) == 1:
            key[sixes[index]] = 6
            del(sixes[index])
            break
    #get 3
    for index in range(len(fives)):
        if len(diff(c[0], fives[index])) == 2:
            key[fives[index]] = 3
            del fives[index]
            break
    #get 9
    for index in range(len(sixes)):
        if len(diff(c[2], sixes[index])) == 4:
            key[sixes[index]] = 9
            del(sixes[index])
            break
    #get 0
    key[sixes[0]] = 0
    #get 2
    for index in range(len(fives)):
        if len(diff(c[2], fives[index])) == 2:
            key[fives[index]] = 2
            del fives[index]
            break
    #get 5
    key[fives[0]] = 5

    total = 0
    for digit in cypher[1]:
        total *= 10
        total += key[digit]
    gtot += total
    
print(gtot)
