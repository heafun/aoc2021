file = open("../inputs/day_1-10/day8.txt")
lines = file.readlines()

count = 0

for line in lines:
    outputParts = line.split("|")[1].strip().split()
    for part in outputParts:
        if (2 <= len(part) <= 4) or len(part)==7:
            count += 1

print(count)
