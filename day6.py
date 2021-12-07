file = open("inputs/day6.txt")
inputState = file.readline().strip().split(",")

for fish in range(len(inputState)):
    inputState[fish] = int(inputState[fish])

for day in range(80):
    for num in range(len(inputState)):
        if inputState[num] == 0:
            inputState.append(8)
            inputState[num] = 6
        else:
            inputState[num] -= 1

print(len(inputState))
