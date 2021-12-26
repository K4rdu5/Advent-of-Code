#Day 8 part 1

#easy
#     "1" : 2
#     "4" : 4
#     "7" : 3
#     "8" : 7

with open("DataDay8.txt", "r") as f:
    lines = f.readlines()

def difficulty(lst):
    hard = []
    easy = []
    for line in lst:
        inp, outp = line.split("|")
        inp, outp = inp.split(), outp.split()
        for out in outp:
            if len(out) in [2,4,3,7]:
                easy.append(out)
            else:
                hard.append(out)
    return easy, hard

print(len(difficulty(lines)[0]))
