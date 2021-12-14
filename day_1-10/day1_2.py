file = open("../inputs/day_1-10/day1.txt")
lines = file.readlines()

for line in range(0, len(lines)):
    lines[line] = int(lines[line])

count = 0
for segment in range(0, len(lines)-3):
    part1 = [lines[segment], lines[segment+1], lines[segment+2]]
    part2 = [lines[segment+1], lines[segment+2], lines[segment+3]]
    if sum(part1) < sum(part2):
        count += 1

print(count)

file.close()