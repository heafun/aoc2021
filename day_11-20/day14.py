file = open("../inputs/day_11-20/day14.txt")
lines = file.readlines()

template = lines[0].strip()
insertionRules = {}

for line in range(2, len(lines)):
    parts = lines[line].strip().split(" -> ")
    insertionRules[parts[0].strip()] = parts[1].strip()

for step in range(10):
    newTemplate = ""
    for i in range(len(template) - 1):
        newTemplate += template[i] + insertionRules[template[i] + template[i + 1]]
    template = newTemplate + template[-1]

characters = list(set(template))
charCount = [0] * len(characters)

for char in template:
    charCount[characters.index(char)] += 1

print(max(charCount) - min(charCount))
