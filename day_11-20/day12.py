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


def recStep(nodes, node: NodeInterface, path):
    if node.id == "end":
        # print(path + node.id)
        return 1

    node.visit()
    sum = 0
    for neighbour in node.adjacentNodes:
        if not neighbour.visited:
            nodesCopy = copy.deepcopy(nodes)
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
