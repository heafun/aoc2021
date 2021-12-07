import numpy as np

file = open("inputs/day6.txt")
inputState = file.readline().strip().split(",")

state = np.zeros(9)

for fish in range(len(inputState)):
    inputState[fish] = int(inputState[fish])
    state[inputState[fish]] += 1

for day in range(256):
    newState = np.zeros(9)
    newState[6] = state[0]
    newState[8] = state[0]
    for num in range(len(state)-1):
        newState[num] += state[num+1]
    state = newState


print(int(sum(state)))
