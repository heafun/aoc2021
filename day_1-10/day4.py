def checkBingo(numbs):
    winBoard = None
    for board in boards:
        for x in range(0, len(board)):
            col = 0
            row = 0
            for y in range(0, len(board)):
                if board[x][y] in numbs:
                    row += 1
                if board[y][x] in numbs:
                    col += 1
                if col == len(board) or row == len(board):
                    winBoard = board

    if winBoard is None:
        return 0
    else:
        sum = 0
        for row in winBoard:
            for num in row:
                if num not in numbs:
                    sum += int(num)

        print(sum)
        print(numbs[len(numbs)-1])
        return sum * int(numbs[len(numbs)-1])



file = open("../inputs/day_1-10/day4.txt")
lines = file.readlines()

rndNmbs = []

for line in lines.copy():
    if not line.strip():
        break
    rndNmbs.extend(line.strip().split(","))
    lines.remove(line)

boards = []
board = []
for line in lines:
    if not line.strip():
        continue
    else:
        board.append(line.strip().split())
    if len(board)==5:
        boards.append(board)
        board = []

print(boards)
for i in range(0, len(rndNmbs)):
    result = checkBingo(rndNmbs.copy()[:i+1])
    if not result == 0:
        print(result)
        break