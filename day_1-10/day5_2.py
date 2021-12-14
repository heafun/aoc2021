import array

import numpy
import numpy as np


def paintVent(vent, ventMap):
    if vent[0][0] == vent[1][0]:
        start = min(vent[0][1], vent[1][1])
        end = max(vent[0][1], vent[1][1])
        row = vent[0][0]

        for i in range(start, end + 1):
            ventMap[row][i] += 1
    elif vent[0][1] == vent[1][1]:
        start = min(vent[0][0], vent[1][0])
        end = max(vent[0][0], vent[1][0])
        col = vent[0][1]

        for i in range(start, end + 1):
            ventMap[i][col] += 1
    else:
        x = vent[0][0]
        y = vent[0][1]
        stepX = 1
        stepY = 1
        if x > vent[1][0]:
            stepX = -1
        if y > vent[1][1]:
            stepY = -1
        x -= stepX
        y -= stepY

        while x != vent[1][0]:
            x += stepX
            y += stepY
            ventMap[x][y] += 1


file = open("../inputs/day_1-10/day5.txt")
lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip().split(" -> ")
    for part in range(len(lines[line])):
        lines[line][part] = lines[line][part].strip().split(",")
        for num in range(len(lines[line][part])):
            lines[line][part][num] = int(lines[line][part][num])

maxSize = 0

for line in range(len(lines)):
    for part in range(len(lines[line])):
        for num in range(len(lines[line][part])):
            if lines[line][part][num] > maxSize:
                maxSize = lines[line][part][num]

ventMap = numpy.zeros((maxSize + 1, maxSize + 1))

for line in lines:
    paintVent(line, ventMap)

dangerZones = 0

for row in ventMap:
    for num in row:
        if num > 1:
            dangerZones += 1

print(dangerZones)
