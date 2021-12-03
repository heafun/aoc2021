def invert(input):
    output = ""

    for letter in input:
        if letter == "1":
            output += "0"
        else:
            output += "1"
    return output


file = open("inputs/day3.txt")
lines = file.readlines()

gamma = ""

for i in range(0, len(lines[0].strip())):
    count = 0
    for line in lines:
        if line[i] == "0":
            count += 1
    if count > len(lines) / 2:
        gamma += "0"
    else:
        gamma += "1"

epsilon = invert(gamma)

print(int(gamma, 2) * int(epsilon, 2))

file.close()
