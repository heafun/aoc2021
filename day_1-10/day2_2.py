file = open("../inputs/day_1-10/day2.txt")
lines = file.readlines()

hPos = 0
depth = 0
aim = 0

for line in lines:
    line = line.strip()
    line = line.split()
    if line[0] == "forward":
        hPos += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])

print(hPos*depth)

file.close()