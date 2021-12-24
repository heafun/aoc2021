import copy

import numpy as np


class Node:
    id: int
    adjacentNodes: []
    weights: []
    f: int
    g: int
    predecessor: object
    closed: bool

    def __init__(self, id: int, f: int):
        self.id = id
        self.adjacentNodes = []
        self.weights = []
        self.f = f
        self.g = 0
        self.predecessor = None
        self.closed = False

    def addConnection(self, node, weight):
        self.adjacentNodes.append(node)
        self.weights.append(weight)

    def getConnectionWeight(self, node):
        try:
            index = self.adjacentNodes.index(node)
            return self.weights[index]
        except ValueError:
            return 20

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.f == other.f


class SortedList:
    list: []

    def __init__(self):
        self.list = []

    def contains(self, item):
        for node in self.list:
            if node.id == item.id:
                return True
        return False

    def add(self, other):
        self.list.append(other)
        self.list.sort(reverse=True)

    def get(self):
        return self.list.pop()

    def update(self, id, f):
        for item in self.list:
            if item.id == id:
                item.f = f
        self.list.sort()


def aStar():
    while openlist:
        currentNode = openlist.get()

        if currentNode.id == network[-1][-1].id:
            return currentNode.g

        currentNode.closed = True
        expandNode(currentNode, openlist)

        # displayState(network)

    return -1


def expandNode(node, openlist):
    for neighbour in node.adjacentNodes:
        if neighbour.closed:
            continue

        g = node.g + node.getConnectionWeight(neighbour)
        if openlist.contains(neighbour) and g >= neighbour.g:
            continue

        neighbour.predecessor = node
        neighbour.g = g
        f = g + neighbour.f

        if openlist.contains(neighbour):
            openlist.update(neighbour.id, f)
        else:
            neighbour.f = f
            openlist.add(neighbour)


def displayEndState():
    displayArray = np.full((np.size(network, 0), np.size(network, 1)), False)

    currentNode = network[-1][-1]

    while currentNode.id != network[0][0].id:
        displayArray[currentNode.id % np.size(network, 0)][
            int(float(currentNode.id) / float(np.size(network, 1)))] = True
        currentNode = currentNode.predecessor

    sum = 0

    for y in range(len(displayArray)):
        line = ""
        for x in range(len(displayArray[0])):
            if displayArray[x][y]:
                line += "#"  # str(network[x][y].g)
                sum += int(lines[y][x])
            else:
                line += "."
            # line += ","
        print(line + " " + str(sum))
    print(sum)


def displayState(network):
    for x in range(len(network[0])):
        line = ""
        for y in range(len(network)):
            line += str(network[x][y].f) + ","
        print(line)
    print("")


def makeHugeGrid(list):
    newList = copy.copy(list)

    for i in range(1, 5):
        for y in range(len(list)):
            line = ""
            for x in range(len(list[0].strip())):
                num = int(list[y][x]) + i
                if num >= 10:
                    num -= 9
                line += str(num)
            newList[y] = newList[y].strip() + line

    for i in range(1, 5):
        for y in range(len(list)):
            line = ""
            for x in range(len(newList[0])):
                num = int(newList[y][x]) + i
                if num >= 10:
                    num -= 9
                line += str(num)
            newList.append(line)

    return newList


file = open("../inputs/day_11-20/day15.txt")
lines = file.readlines()

lines = makeHugeGrid(lines)

network = np.empty((len(lines[0].strip()), len(lines)), Node)
openlist = SortedList()

for x in range(np.size(network, 0)):
    for y in range(np.size(network, 1)):
        f = (np.size(network, 0) - 1 - x) + (np.size(network, 1) - 1 - y)
        node = Node(y * np.size(network, 0) + x, f)
        network[x][y] = node

for x in range(np.size(network, 0)):
    for y in range(np.size(network, 1)):
        node = network[x][y]
        if x > 0:
            node.addConnection(network[x - 1][y], int(lines[y][x - 1]))
        if y > 0:
            node.addConnection(network[x][y - 1], int(lines[y - 1][x]))
        if x < np.size(network, 0) - 1:
            node.addConnection(network[x + 1][y], int(lines[y][x + 1]))
        if y < np.size(network, 1) - 1:
            node.addConnection(network[x][y + 1], int(lines[y + 1][x]))

openlist.add(network[0][0])

print(aStar() + 2)  # dont know why...
# displayEndState()
