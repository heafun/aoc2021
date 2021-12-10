def islowpoint(row, col):
    if row - 1 >= 0 and heightmap[row][col] >= heightmap[row - 1][col]:
        return False
    elif row + 1 < len(heightmap) and heightmap[row][col] >= heightmap[row + 1][col]:
        return False
    elif col-1>=0 and heightmap[row][col] >= heightmap[row][col-1]:
        return False
    elif col+1 < len(heightmap[row]) and heightmap[row][col] >= heightmap[row][col+1]:
        return False
    else:
        return True


file = open("inputs/day9.txt")
lines = file.readlines()

heightmap = []

for line in lines:
    row = []
    for num in line.strip():
        row.append(int(num))
    heightmap.append(row)

riskSum = 0

for row in range(len(heightmap)):
    for col in range(len(heightmap[row])):
        if islowpoint(row, col):
            riskSum += 1 + heightmap[row][col]

print(riskSum)
