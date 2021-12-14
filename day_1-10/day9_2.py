def islowpoint(row, col):
    if row - 1 >= 0 and heightmap[row][col] >= heightmap[row - 1][col]:
        return False
    elif row + 1 < len(heightmap) and heightmap[row][col] >= heightmap[row + 1][col]:
        return False
    elif col - 1 >= 0 and heightmap[row][col] >= heightmap[row][col - 1]:
        return False
    elif col + 1 < len(heightmap[row]) and heightmap[row][col] >= heightmap[row][col + 1]:
        return False
    else:
        return True


def getbasinsize(row, col):
    visited = []
    queue = []
    visited.append([row, col])
    queue.append([row, col])

    size = 0

    while len(queue) > 0:
        size += 1
        point = queue.pop(0)
        if point[0] - 1 >= 0 and [point[0] - 1, point[1]] not in visited and heightmap[point[0] - 1][point[1]] != 9:
            visited.append([point[0] - 1, point[1]])
            queue.append([point[0] - 1, point[1]])
        if point[0] + 1 < len(heightmap) and [point[0] + 1, point[1]] not in visited and heightmap[point[0] + 1][
            point[1]] != 9:
            visited.append([point[0] + 1, point[1]])
            queue.append([point[0] + 1, point[1]])
        if point[1] - 1 >= 0 and [point[0], point[1] - 1] not in visited and heightmap[point[0]][point[1] - 1] != 9:
            visited.append([point[0], point[1] - 1])
            queue.append([point[0], point[1] - 1])
        if point[1] + 1 < len(heightmap[point[0]]) and [point[0], point[1] + 1] not in visited and heightmap[point[0]][
            point[1] + 1] != 9:
            visited.append([point[0], point[1] + 1])
            queue.append([point[0], point[1] + 1])

    return size


file = open("../inputs/day_1-10/day9.txt")
lines = file.readlines()

heightmap = []

for line in lines:
    row = []
    for num in line.strip():
        row.append(int(num))
    heightmap.append(row)

basinsizes = []

for row in range(len(heightmap)):
    for col in range(len(heightmap[row])):
        if islowpoint(row, col):
            basinsizes.append(getbasinsize(row, col))

basinsizes.sort(reverse=True)

print(basinsizes[0] * basinsizes[1] * basinsizes[2])
