import numpy as np
import math

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day11/input.txt', 'r').read().splitlines()

def partOne():
    charArray = np.full((len(lines), len(lines[0])), '.', dtype=np.dtype('U1'))

    pairCoords = []
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == '#':
                pairCoords.append((i, j))
                charArray[i][j] = '#'

    doubledRows = []
    for i, l in enumerate(charArray):
        if '#' not in l:
            doubledRows.append(i)
            for j in range(len(charArray[i])):
                charArray[i][j] = '2'

    doubledCols = []
    for j in range(len(charArray[0])):
        col = column(charArray, j)
        if '#' not in col:
            doubledCols.append(j)
            for i in range(len(col)):
                charArray[i][j] = '2'

    print(pairCoords)
    print(charArray)
    print(doubledCols)

    sum = 0
    for i in range(len(pairCoords)):
        r1, c1 = pairCoords[i]
        for j in range(i + 1, len(pairCoords)):
            r2, c2 = pairCoords[j]
            cdif = abs(c2 - c1)
            rdif = abs(r2 - r1)
            
            # now count the expanded rows/columns
            expansionSize = 1000000 - 1 # make this 2 for part1
            if c1 < c2:
                for c in range(c1, c2):
                    if c in doubledCols:
                        cdif += expansionSize
            else:
                for c in range(c2, c1):
                    if c in doubledCols:
                        cdif += expansionSize

            if r1 < r2:
                for r in range(r1, r2):
                    if r in doubledRows:
                        rdif += expansionSize
            else:
                for r in range(r2, r1):
                    if r in doubledRows:
                        rdif += expansionSize
                           
            sum += (cdif + rdif)
            #print('coord 1: ' + str(r1) + ',' + str(c1) + ' coord 2: ' + str(r2) + ',' + str(c2) + ' rdif: ' + str(rdif) + ' cdif: ' + str(cdif))
            
    print(sum)


def column(matrix, i):
    return [row[i] for row in matrix]

partOne()