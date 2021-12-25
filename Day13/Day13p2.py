#Day 13 part 2
import numpy as np

with open("DataDay13.txt", "r") as f:
    data = [line for line in f.read().split()]

def paper(data):
    paper = np.zeros((895,1311))
    for points in data[:799]:
        x, y = points.split(",")
        paper[int(y)][int(x)] = 1
    return paper

paper1 = paper(data).transpose()[:655]
paper2 = paper(data).transpose()[656:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

paper1 = foldedpaper[:447]
paper2 = np.flipud(foldedpaper[448:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper.transpose()[:327]
paper2 = foldedpaper.transpose()[328:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

paper1 = foldedpaper[:223]
paper2 = np.flipud(foldedpaper[224:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper.transpose()[:163]
paper2 = foldedpaper.transpose()[164:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

paper1 = foldedpaper[:111]
paper2 = np.flipud(foldedpaper[112:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper.transpose()[:81]
paper2 = foldedpaper.transpose()[82:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

paper1 = foldedpaper[:55]
paper2 = np.flipud(foldedpaper[56:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper.transpose()[:40]
paper2 = foldedpaper.transpose()[41:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

paper1 = foldedpaper[:27]
paper2 = np.flipud(foldedpaper[28:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper[:13]
paper2 = np.flipud(foldedpaper[14:])
foldedpaper = paper1 + paper2

paper1 = foldedpaper[:6]
paper2 = np.flipud(foldedpaper[7:])
foldedpaper = paper1 + paper2

i = 0
for line in foldedpaper:
    j = 0
    for num in line:
        if num != 0. and num != 1.:
            foldedpaper[i][j] = 1.
        j += 1
    i += 1

for i in range(8):
    for num in foldedpaper:
        print(num[i*5:i*5+4])
    print("-------")
