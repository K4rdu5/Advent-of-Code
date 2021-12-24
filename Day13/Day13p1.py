#Day 13 part 1
import numpy as np

with open("DataDay13.txt", "r") as f:
    data = [line for line in f.read().split()]


def paper(data):
    paper = np.zeros((1070,1311))
    for points in data[:799]:
        x, y = points.split(",")
        paper[int(y)][int(x)] = 1
    return paper

paper1 = paper(data).transpose()[:655]
paper2 = paper(data).transpose()[656:]
paper2 = np.fliplr(paper2.transpose())
foldedpaper = paper1.transpose() + paper2

i = 0
for line in foldedpaper:
    j = 0
    for num in line:
        if num != 0. and num != 1.:
            foldedpaper[i][j] = 1.
        j += 1
    i += 1

int(sum(foldedpaper).cumsum()[len(sum(foldedpaper).cumsum())-1])
