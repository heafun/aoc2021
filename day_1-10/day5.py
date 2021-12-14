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
    else:
        start = min(vent[0][0], vent[1][0])
        end = max(vent[0][0], vent[1][0])
        col = vent[0][1]

        for i in range(start, end + 1):
            ventMap[i][col] += 1


file = open("../inputs/day_1-10/day5.txt")
lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip().split(" -> ")
    for part in range(len(lines[line])):
        lines[line][part] = lines[line][part].strip().split(",")
        for num in range(len(lines[line][part])):
            lines[line][part][num] = int(lines[line][part][num])

lines = np.array(lines)

filter_arr = []

for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

lines = lines[filter_arr]

maxSize = 0

for line in range(len(lines)):
    for part in range(len(lines[line])):
        for num in range(len(lines[line][part])):
            if lines[line][part][num] > maxSize:
                maxSize = lines[line][part][num]

ventMap = numpy.zeros((maxSize+1, maxSize+1))

for line in lines:
    paintVent(line, ventMap)

dangerZones = 0

for row in ventMap:
    for num in row:
        if num > 1:
            dangerZones+=1

print(dangerZones)
