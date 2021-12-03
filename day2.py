file = open("inputs/day2.txt")
lines = file.readlines()

hPos = 0
depth = 0

for line in lines:
    line = line.strip()
    line = line.split()
    if line[0] == "forward":
        hPos += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])

print(hPos*depth)

file.close()