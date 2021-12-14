import sys

file = open("../inputs/day_1-10/day7.txt")
line = file.readline().strip().split(",")


for sub in range(len(line)):
    line[sub] = int(line[sub])

maxPos = max(line)

cheapest = sys.maxsize

for i in range(maxPos+1):
    fuelCost = 0
    for sub in line:
        fuelCost += abs(i-sub)
    if cheapest > fuelCost:
        cheapest = fuelCost

print(cheapest)
