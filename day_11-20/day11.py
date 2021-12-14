def flash(row, col):
    grid[row][col] = 11

    for r in range(max(row - 1, 0), min(row + 2, len(grid))):
        for c in range(max(col - 1, 0), min(col + 2, len(grid[0]))):
            if r != row or c != col:
                if grid[r][c] != 10 and grid[r][c] != 11:
                    grid[r][c] += 1


def step(total):
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
                total += 1
                break
            c += 1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 11:
                grid[r][c] = 0

    return total


file = open("../inputs/day_11-20/day11.txt")
lines = file.readlines()

result = 0
grid = []

for line in lines:
    row = []
    for num in line.strip():
        row.append(int(num))
    grid.append(row)

for i in range(100):
    result = step(result)

print(result)
