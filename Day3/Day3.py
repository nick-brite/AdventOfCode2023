import numpy as np

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day3/input.txt', 'r').read().splitlines()

def partOne():
    symbolMatrix = np.zeros((len(lines), len(lines[0])))
    sumOfParts = 0
    
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if not (c.isdigit() or c == '.'):
                symbolMatrix[i][j] = -1


    for i, l in enumerate(lines):
        j = 0
        while j < len(l) :
            c = l[j]
            if c.isdigit():
                numberStr = c
                isNeighbor = isSymbolNeighbor(i, j, symbolMatrix)

                incr = 1 # grab rest of number
                while (j + incr < len(l) and l[j+incr].isdigit()):
                    numberStr += l[j+incr]
                    if not isNeighbor:
                        isNeighbor = isSymbolNeighbor(i, j + incr, symbolMatrix)
                    incr += 1

                if (isNeighbor):
                    sumOfParts += int(numberStr)
                j = j + incr # skip to end of word
            else: 
                j = j + 1

    print(sumOfParts)

def isSymbolNeighbor(row, column, symbolMatrix):
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if r > -1 and c > -1 and r < len(symbolMatrix) and c < len(symbolMatrix[0]) and symbolMatrix[r, c] == -1:
                return True
    return False

def partTwo():
    numberMatrix = np.zeros((len(lines), len(lines[0])))
    sumOfGearRatios = 0
    
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c.isdigit():
                numberMatrix[i][j] = -1

    for i, l in enumerate(lines):
        for j, c in enumerate(l) :
            if c == '*':
                sumOfGearRatios += getGearRatio(i, j, numberMatrix)

    print(sumOfGearRatios)

def getGearRatio(row, column, numberMatrix):
    numNeighbors = 0
    neighbors = []

    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if r > -1 and c > -1 and r < len(numberMatrix) and c < len(numberMatrix[0]) and numberMatrix[r, c] == -1:
                duplicateNeighbor = False
                for i, j in neighbors: # ensure you're not double counting the same neighbor
                    if isSameWord((i, j), (r, c)):
                        duplicateNeighbor = True

                if not duplicateNeighbor:
                    numNeighbors = numNeighbors + 1
                    neighbors.append((r, c))

    if numNeighbors != 2:
        return 0
    else:
        gearRatio = 1
        for i, j in neighbors:
            # find value of each number neighbor and multiple them together to get gear number
            word = lines[i][j]

            incr = 1 # add characters after
            while j+incr < len(lines[i]) and lines[i][j+incr].isdigit():
                word = word + lines[i][j+incr]
                incr += 1
            
            incr = -1 # add characters before
            while j + incr >= 0 and lines[i][j+incr].isdigit():
                word = lines[i][j+incr] + word
                incr -= 1

            gearRatio *= int(word)

    return gearRatio

def isSameWord(tuple1, tuple2):
    if tuple1[0] == tuple2[0]:
        for c in range(tuple1[1], tuple2[1] + 1):
            if lines[tuple1[0]][c] == '.' or lines[tuple1[0]][c] == '*':
                return False
        return True
    return False

partTwo()