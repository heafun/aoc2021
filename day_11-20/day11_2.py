def flash(row, col):
    grid[row][col] = 11

    for r in range(max(row - 1, 0), min(row + 2, len(grid))):
        for c in range(max(col - 1, 0), min(col + 2, len(grid[0]))):
            if r != row or c != col:
                if grid[r][c] != 10 and grid[r][c] != 11:
                    grid[r][c] += 1


def step():
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 10:
                grid[r][c] += 1

    r = -1
    while r < len(grid)-1:
        r += 1
        c = 0
        while c < len(grid[0]):
            if grid[r][c] == 10:
                flash(r, c)
                r = -1
                c = 0
                break
            c += 1

    inSync = True

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 11:
                grid[r][c] = 0
            else:
                inSync = False

    return inSync


file = open("../inputs/day_11-20/day11.txt")
lines = file.readlines()

grid = []

for line in lines:
    row = []
    for num in line.strip():
        row.append(int(num))
    grid.append(row)

stepCount = 0
result = False

while not result:
    result = step()
    stepCount += 1

print(stepCount)
