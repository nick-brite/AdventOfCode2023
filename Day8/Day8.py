import numpy as np
import math

lines = open('/Users/nickalbright/Projects/AdventOfCode2023/Day8/input.txt', 'r').read().splitlines()
nodeList = []

class Node:
    def __init__(self, tag, leftNode, rightNode):
        self.tag = tag
        self.leftNode = leftNode
        self.rightNode = rightNode

def partOne():
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

def partTwo():
    startingNodes = []
    for l in lines[2:]:
        split = l.split(' = ')
        secondSplit = split[1].split(',')
        node = Node(split[0], secondSplit[0].strip()[1:], secondSplit[1].strip()[:-1])
        if node.tag[2] == 'A':
            startingNodes.append(node)
        
        nodeList.append(node)

    stepLengths = []
    for node in startingNodes:
        steps = 0
        newNode = node
        while newNode.tag[2] != 'Z':
            for c in lines[0]:
                steps += 1
                if c == 'L':
                    newNodeTag = newNode.leftNode 
                elif c == 'R':
                    newNodeTag = newNode.rightNode

                newNode = [node for node in nodeList if node.tag == newNodeTag][0]
                if newNode.tag[2] == 'Z':
                    stepLengths.append(steps)
                    break

    print(math.lcm(*stepLengths))


partTwo()