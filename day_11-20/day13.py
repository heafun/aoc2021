import numpy as np


def fold(paper, foldLine: str):
    direction = foldLine.strip().split("=")[0]
    foldPos = int(foldLine.strip().split("=")[1])

    if direction == "x":
        result = np.full((foldPos, np.size(paper, 1)), False)

        for x in range(foldPos + 1, np.size(paper, 0)):
            for y in range(np.size(paper, 1)):
                if paper[x][y]:
                    result[foldPos - abs(x - foldPos)][y] = True
                if paper[x - foldPos - 1][y]:
                    result[x - foldPos - 1][y] = True
    else:
        result = np.full((np.size(paper, 0), foldPos), False)

        for x in range(np.size(paper, 0)):
            for y in range(foldPos + 1, np.size(paper, 1)):
                if paper[x][y]:
                    result[x][foldPos - abs(y - foldPos)] = True

                if paper[x][y - foldPos - 1]:
                    result[x][y - foldPos - 1] = True

    return result


def prettify(list):
    result = ""
    for y in range(np.size(list, 1)):
        for x in range(np.size(list, 0)):
            if list[x][y]:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result


file = open("../inputs/day_11-20/day13.txt")
lines = file.readlines()

maxX = 0
maxY = 0

for line in lines:
    if not line.strip():
        break
    else:
        coords = line.strip().split(",")
        if int(coords[0]) > maxX:
            maxX = int(coords[0])
        if int(coords[1]) > maxY:
            maxY = int(coords[1])

points = np.full((maxX + 1, maxY + 1), False)
folds = []

for line in lines:
    if not line.strip():
        continue
    elif line.strip().startswith("fold"):
        folds.append(line.strip().split()[-1])
    else:
        coords = line.strip().split(",")
        points[int(coords[0])][int(coords[1])] = True

print(np.count_nonzero(fold(points, folds[0])))
