def getPoints(character):
    switcher = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    return switcher.get(character)


file = open("../inputs/day_1-10/day10.txt")
lines = file.readlines()

openings = ["(", "{", "[", "<"]
closings = [")", "}", "]", ">"]

lineScore = []

for line in range(len(lines)):
    lines[line] = lines[line].strip()
    keep = True
    openList = []
    for char in lines[line]:
        if char in openings:
            openList.append(char)
        else:
            lastOpen = openList.pop()
            if openings.index(lastOpen) != closings.index(char):
                keep = False
                break
    if keep:
        score = 0
        while len(openList) != 0:
            char = openList.pop()
            score *= 5
            score += getPoints(char)
        lineScore.append(score)

lineScore.sort()

print(lineScore[int(len(lineScore) / 2)])
