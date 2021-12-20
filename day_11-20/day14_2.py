file = open("../inputs/day_11-20/day14.txt")
lines = file.readlines()

template = {}
insertionRules = {}

characters = ""

for line in range(2, len(lines)):
    parts = lines[line].strip().split(" -> ")
    characters += parts[0] + parts[1]
    insertionRules[parts[0].strip()] = [parts[0][0] + parts[1].strip(), parts[1].strip() + parts[0][1]]
    template[parts[0].strip()] = 0

characters = list(set(characters))
charCount = {}

for char in characters:
    charCount[char] = 0

for char in range(len(lines[0].strip()) - 1):
    template[lines[0][char] + lines[0][char + 1]] += 1
    charCount[lines[0][char]] += 1
charCount[lines[0].strip()[-1]] += 1

for step in range(40):
    newTemplate = template.copy()
    for combi in template:
        if template[combi] > 0:
            rule = insertionRules[combi]
            newTemplate[combi] -= template[combi]
            newTemplate[rule[0]] += template[combi]
            newTemplate[rule[1]] += template[combi]
            charCount[rule[0][1]] += template[combi]
    template = newTemplate

print(max(charCount.values()) - min(charCount.values()))
