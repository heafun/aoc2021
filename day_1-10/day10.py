def getPoints(character):
    switcher = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return switcher.get(character)


file = open("../inputs/day_1-10/day10.txt")
lines = file.readlines()

openList = []
openings = ["(", "{", "[", "<"]
closings = [")", "}", "]", ">"]

score = 0

for line in range(len(lines)):
    lines[line] = lines[line].strip()
    keep = True
    for char in lines[line]:
        if char in openings:
            openList.append(char)
        else:
            lastOpen = openList.pop()
            if openings.index(lastOpen) != closings.index(char):
                score += getPoints(char)
                keep = False
                break
    if keep:
        print(str(line) + ": " + lines[line])

print(score)
