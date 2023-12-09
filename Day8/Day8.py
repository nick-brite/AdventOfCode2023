import numpy as np

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day8/input.txt', 'r').read().splitlines()

class Node:
    def __init__(self, tag, leftNode, rightNode):
        self.tag = tag
        self.leftNode = leftNode
        self.rightNode = rightNode

def partOne():
    nodeList = []
    firstNode = None
    for l in lines[2:]:
        split = l.split(' = ')
        secondSplit = split[1].split(',')
        node = Node(split[0], secondSplit[0].strip()[1:], secondSplit[1].strip()[:-1])
        if node.tag == 'AAA':
            firstNode = node

        nodeList.append(node)

    steps = 0
    newNode = firstNode
    while newNode.tag != 'ZZZ':
        for c in lines[0]:
            steps += 1
            if c == 'L':
                newNodeTag = newNode.leftNode 
            elif c == 'R':
                newNodeTag = newNode.rightNode

            newNode = [node for node in nodeList if node.tag == newNodeTag][0]
            if newNode.tag == 'ZZZ':
                break

    print(steps)


partOne()