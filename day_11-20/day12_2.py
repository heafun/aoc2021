import copy


class NodeInterface:
    adjacentNodes = []
    visited = False
    id = ""

    def __init__(self, nodeId):
        self.id = nodeId
        self.adjacentNodes = []

    def addAdjacent(self, node):
        self.adjacentNodes.append(node)

    def visit(self):
        pass

    def isVisited(self) -> bool:
        return self.visited


class smallNode(NodeInterface):

    def visit(self):
        self.visited = True


class mediumNode(NodeInterface):
    visits = 0

    def visit(self):
        self.visits += 1
        if self.visits >= 2:
            self.visited = True


class bigNode(NodeInterface):
    visits = 0

    def visit(self):
        self.visits += 1


def getObject(list, key, index=False):  # index true: return index; false: return object
    for entry in range(len(list)):
        if list[entry].id == key:
            if index:
                return entry
            else:
                return list[entry]


def containsMedium(list, getObject=False):
    for node in list:
        if type(node) is mediumNode:
            if getObject:
                return node
            else:
                return True
    return False


def insertNewNode(list, newNode, index):
    list[index] = newNode

    for node in list:
        for neighbour in range(len(node.adjacentNodes)):
            if node.adjacentNodes[neighbour].id == newNode.id:
                node.adjacentNodes[neighbour] = newNode


def recStep(nodes, node: NodeInterface, path):
    if node.id == "end":
        if not containsMedium(nodes):
            # print(path + node.id)
            return 1
        else:
            medium = containsMedium(nodes, True)

            if path.count("-" + medium.id + "-") == 2:
                # print(medium.id + ": " + path + node.id)
                return 1
            else:
                return 0

    node.visit()
    sum = 0
    for neighbour in node.adjacentNodes:
        if not neighbour.visited:
            nodesCopy = copy.deepcopy(nodes)
            if not containsMedium(nodesCopy) and type(neighbour) is smallNode \
                    and neighbour.id != "start" and neighbour.id != "end":
                newNetwork = copy.deepcopy(nodes)
                nodeIndex = getObject(newNetwork, neighbour.id, True)
                newNode = mediumNode(neighbour.id)
                for adjacent in neighbour.adjacentNodes:
                    newNode.addAdjacent(getObject(newNetwork, adjacent.id))
                insertNewNode(newNetwork, newNode, nodeIndex)
                sum += recStep(newNetwork, newNode, path + node.id + "-")

            sum += recStep(nodesCopy, getObject(nodesCopy, neighbour.id), path + node.id + "-")
    return sum


file = open("../inputs/day_11-20/day12.txt")
lines = file.readlines()
nodes = []

for line in lines:
    parts = line.strip().split("-")
    for part in parts:
        if not any(obj.id == part for obj in nodes):
            if part.isupper():
                nodes.append(bigNode(part))
            else:
                nodes.append(smallNode(part))

for line in lines:
    parts = line.strip().split("-")
    node1 = getObject(nodes, parts[0])
    node2 = getObject(nodes, parts[1])
    node1.addAdjacent(node2)
    node2.addAdjacent(node1)

start = getObject(nodes, "start")

paths = recStep(nodes, start, "")

print(paths)
