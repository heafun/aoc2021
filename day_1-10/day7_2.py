import sys

file = open("../inputs/day_1-10/day7.txt")
line = file.readline().strip().split(",")


def cost(steps):
    return sum(range(1, steps+1))


for sub in range(len(line)):
    line[sub] = int(line[sub])

maxPos = max(line)

cheapest = sys.maxsize
cheapestPos = 0
avg = int(sum(line) / len(line))
section = int(len(line) * 0.2)

for i in range(avg - section, avg + section):
    fuelCost = 0
    for sub in line:
        fuelCost += cost(abs(i-sub))
    if cheapest > fuelCost:
        cheapest = fuelCost
        cheapestPos = i

print(cheapest)
print("at " + str(cheapestPos))
print("Avg: " + str(avg))
