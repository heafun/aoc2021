file = open("../inputs/day_1-10/day8.txt")
lines = file.readlines()

def sort(string):
    string = sorted(string)
    return "".join(string)

def missing(num1, num2):
    miss = 0

    for seg in num2:
        if seg not in num1:
            miss += 1

    return miss

def solveLine(case):
    numbers = [None] * 10
    five = []
    six = []

    for num in case[0]:
        if len(num) == 2:
            numbers[1] = num
        elif len(num) == 3:
            numbers[7] = num
        elif len(num) == 4:
            numbers[4] = num
        elif len(num) == 5:
            five.append(num)
        elif len(num) == 6:
            six.append(num)
        elif len(num) == 7:
            numbers[8] = num

    for num in six:
        if missing(num, numbers[1]) > 0:
            numbers[6] = num
        elif missing(num, numbers[4]) > 0:
            numbers[0] = num
        else:
            numbers[9] = num

    for num in five:
        if missing(num, numbers[1]) == 0:
            numbers[3] = num
        elif missing(num, numbers[4]) == 1:
            numbers[5] = num
        else:
            numbers[2] = num

    for num in range(len(numbers)):
        numbers[num] = sort(numbers[num])

    output = ""
    for num in range(len(case[1])):
        case[1][num] = sort(case[1][num])
        output += str(numbers.index(case[1][num]))

    return int(output)


count = 0
line = []
result = 0

for l in range(len(lines)):
    line.append(lines[l].strip().split("|"))
    line[l][0] = line[l][0].strip().split()
    line[l][1] = line[l][1].strip().split()
    result += solveLine(line[l])

print(result)
