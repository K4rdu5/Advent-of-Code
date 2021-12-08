#Day 8 part 1
with open("DataDay8.txt", "r") as f:
    lines = f.read().split("\n")

def difficulty(lst):
    hard=[]
    easy = []
    for line in lst:
        inp, outp = line.split("|")
        inp, outp = inp.split(), outp.split()
        for out in outp:
            if len(out) == 2 or len(out) == 3 or len(out) == 4 or len(out) == 7:
                easy.append(out)
            else:
                hard.append(out)
    return easy, hard

print(len(difficulty(lines)[0]))
