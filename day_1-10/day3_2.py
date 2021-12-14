import copy


def filter(index, keep, list):
    i = 0
    while i < len(list):
        if len(list) == 1:
            return
        elif not list[i][index] == keep:
            list.pop(i)
        else:
            i += 1


def getRating(most, list):
    for i in range(0, len(list[0].strip())):
        if len(list) == 1:
            return
        count = 0
        for line in list:
            if line[i] == "0":
                count += 1
        if count > len(list) / 2:
            if most:
                filter(i, "0", list)
            else:
                filter(i, "1", list)
        else:
            if most:
                filter(i, "1", list)
            else:
                filter(i, "0", list)


file = open("../inputs/day_1-10/day3.txt")
lines = file.readlines()

oxygen = copy.copy(lines)
co2 = copy.copy(lines)

getRating(True, oxygen)
getRating(False, co2)

print(int(oxygen[0], 2) * int(co2[0], 2))

file.close()
