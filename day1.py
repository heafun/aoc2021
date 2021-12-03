file = open("inputs/day1.txt")
lines = file.readlines()

count = 0
prevline = -1
for line in lines:
    if prevline == -1:
        prevline = int(line)
        continue
    line = int(line)
    if prevline < line:
        count += 1
    prevline = line

print(count)

file.close()