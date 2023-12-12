import numpy as np
import math

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day10/input.txt', 'r').read().splitlines()
stepsArr = []
charMap = []
startPos = None
startChar = None
tubePoints = set()

def partTwo():
    partOne() #sets up data
    # create image

    # create 2d char array
    charArray = np.full((len(lines), len(lines[0])), '.', dtype=np.dtype('U1'))

    for i in range(len(charArray)):
        for j in range(len(charArray[0])):
            charArray[i][j] = lines[i][j]

    charArray[startPos[0]][startPos[1]] = startChar
    newCharArray = charArray

    # now do the thing!
    insideCount = 0
    for i, row in enumerate(charArray):
        wallCount = 0
        c1 = None
        for j, c in enumerate(row):
            if ((i, j) in tubePoints):
                if c == '|':
                    wallCount += 1
                elif c in 'FL':
                    c1 = c # use this for tracking combined walls
                elif c == 'J':
                    if c1 == 'F':
                        wallCount += 1
                        c1 = None
                elif c == '7':
                    if c1 == 'L':
                        wallCount += 1
                    c1 = None

            else:
                if wallCount % 2 == 1:
                    newCharArray[i][j] = 'I'
                    insideCount += 1
                
    #printMap(newCharArray)
    print(insideCount)
            


def printMap(charArray):
    # Specify the file path
    file_path = "output.txt"

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Iterate over each list in the list of lists
        for innerList in charArray:
            # Use the print function to write the inner list to the file
            print(innerList, file=file)


def partOne():
    global startPos
    startPos = (0, 0)
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == 'S':
                startPos = (i, j)

    # track steps
    stepsArr = np.zeros((len(lines), len(lines[0])))
    stepsArr[startPos[0]][startPos[1]] = 0

    # figure out start positions
    path1Pos, nextDir1 = checkPositions(startPos, None)
    path2Pos, nextDir2 = checkPositions(startPos, path1Pos)

    # replace S character (more for P2)
    lineDif1 = path1Pos[0] - startPos[0]
    colDif1 = path1Pos[1] - startPos[1]
    lineDif2 = path2Pos[0] - startPos[0]
    colDif2 = path2Pos[1] - startPos[1]

    startDirs = []
    if lineDif1 == -1:
        startDirs.append('N')
    elif lineDif1 == 1:
        startDirs.append('S')
    elif colDif1 == -1:
        startDirs.append('W')
    elif colDif1 == 1:
        startDirs.append('E')

    if lineDif2 == -1:
        startDirs.append('N')
    elif lineDif2 == 1:
        startDirs.append('S')
    elif colDif2 == -1:
        startDirs.append('W')
    elif colDif2 == 1:
        startDirs.append('E')

    global startChar
    if 'N' in startDirs:
        if 'S' in startDirs:
            startChar = '|'
        elif 'E' in startDirs:
            startChar = 'L'
        elif 'W' in startDirs:
            startChar = 'J'
    elif 'E' in startDirs:
        if 'W' in startDirs:
            startChar = '-'
        elif 'S' in startDirs:
            startChar = 'F'
    elif 'S' in startDirs and 'W' in startDirs:
        startChar = '7'

    global tubePoints
    tubePoints.add(startPos) # For P2
    
    steps = 1
    stepsArr[path1Pos[0]][path1Pos[1]] = steps
    stepsArr[path2Pos[0]][path2Pos[1]] = steps
    tubePoints.add((path1Pos[0], path1Pos[1]))
    tubePoints.add((path2Pos[0], path2Pos[1]))



    while path1Pos != path2Pos:
        steps += 1
        path1Pos = getNextPosition(path1Pos, nextDir1)
        path2Pos = getNextPosition(path2Pos, nextDir2)
        stepsArr[path1Pos[0]][path1Pos[1]] = steps
        stepsArr[path2Pos[0]][path2Pos[1]] = steps
        tubePoints.add((path1Pos[0], path1Pos[1]))
        tubePoints.add((path2Pos[0], path2Pos[1]))


        # coding terribly here: - have to switch directions to be from perspective of called node
        if (nextDir1 == 'N'):
            nextDir1 = 'S'
        elif (nextDir1 == 'S'):
            nextDir1 = 'N'
        elif (nextDir1 == 'E'):
            nextDir1 = 'W'
        elif (nextDir1 == 'W'):
            nextDir1 = 'E'

        if (nextDir2 == 'N'):
            nextDir2 = 'S'
        elif (nextDir2 == 'S'):
            nextDir2 = 'N'
        elif (nextDir2 == 'E'):
            nextDir2 = 'W'
        elif (nextDir2 == 'W'):
            nextDir2 = 'E'
        
        nextDir1 = connects(nextDir1, lines[path1Pos[0]][path1Pos[1]])
        nextDir2 = connects(nextDir2, lines[path2Pos[0]][path2Pos[1]])

    if (path1Pos == path2Pos): # furthest point
        stepsArr[path1Pos[0]][path1Pos[1]] = steps
        tubePoints.add((path1Pos[0], path1Pos[1]))

    print(steps)



def getNextPosition(currPosition, nextDir):
    if nextDir == 'N':
        return currPosition[0] - 1, currPosition[1]
    if nextDir == 'E':
        return currPosition[0], currPosition[1] + 1
    if nextDir == 'W':
        return currPosition[0], currPosition[1] - 1
    if nextDir == 'S':
        return currPosition[0] + 1, currPosition[1]


def checkPositions(position, invalidNode):
    nextDir = None
    if position[0] - 1 >= 0: # check South
        nextLocation = (position[0] - 1, position[1])
        if nextLocation != invalidNode:
            nextDir = connects('S', lines[position[0] - 1] [position[1]])
            if nextDir != None:
                return (position[0] - 1, position[1]), nextDir
    if position[1] + 1 < len(lines[0]): # West
        nextLocation = (position[0], position[1] + 1)
        if nextLocation != invalidNode:
            nextDir = connects('W', lines[position[0]][position[1] + 1])
            if nextDir != None:
                return (position[0], position[1] + 1), nextDir
    if position[0] + 1 < len(lines): # North
        nextLocation = (position[0] + 1, position[1])
        if nextLocation != invalidNode:
            nextDir = connects('N', lines[position[0] + 1][position[1]])
            if nextDir != None:
                return (position[0] + 1, position[1]), nextDir
    if position[1] - 1 >= 0: # East
        nextLocation = (position[0], position[1] - 1)
        if nextLocation != invalidNode:
            nextDir = connects('E', lines[position[0]][position[1] - 1])
            if nextDir != None:
                return (position[0], position[1] - 1), nextDir
    return None




# determines if eligible link. e.g. fromDirection = 'E', '7' connects
def connects(fromDirection, newLink):
    connects = False
    if fromDirection == 'N':
        connects = newLink == '|' or newLink == 'J' or newLink == 'L'
    if not connects and fromDirection == 'E':
        connects = newLink == '-' or newLink == 'F' or newLink == 'L'
    if not connects and fromDirection == 'S':
        connects = newLink == '|' or newLink == 'F' or newLink == '7'
    if not connects and fromDirection == 'W':
        connects = newLink == '-' or newLink == 'J' or newLink == '7'

    if not connects:
        return None
    else:
        # find and return next direction
        if newLink == '|':
            if fromDirection == 'N':
                return 'S'
            else:
                return 'N'
        if newLink == '-':
            if fromDirection == 'E':
                return 'W'
            else:
                return 'E'
        if newLink == 'L':
            if fromDirection == 'N':
                return 'E'
            else:
                return 'N'
        if newLink == 'J':
            if fromDirection == 'N':
                return 'W'
            else:
                return 'N'
        if newLink == 'F':
            if fromDirection == 'S':
                return 'E'
            else:
                return 'S'
        if newLink == '7':
            if fromDirection == 'S':
                return 'W'
            else:
                return 'S'

partTwo()
