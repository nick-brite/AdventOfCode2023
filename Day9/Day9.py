import numpy as np
import math

lines = open('/Users/nickalbright/Projects/AdventOfCode2023/Day9/input.txt', 'r').read().splitlines()

def partOne():
    sumNextVals = 0
    for l in lines:
        highestVals = l.split()
        for i, t in enumerate(highestVals):
            highestVals[i] = int(t)


        allZeros = False
        listList = [] # keep track of hierarchy of lists
        listList.append(highestVals)

        parentVals = highestVals
        childVals = []
        while not allZeros:
            i = 1
            while i < len(parentVals):
                childVals.append(parentVals[i] - parentVals[i-1])
                i += 1
            listList.append(childVals)
                
            allZeros = True
            for v in childVals:
                if v != 0:
                    allZeros = False
                    break

            if not allZeros:
                parentVals = childVals
                childVals = []

        # predict next value
        lowerVal = 0
        for i, l in enumerate(listList[::-1]):
            if i != 0:
                lowerVal = l[-1] + lowerVal

        sumNextVals += lowerVal
        
    print(sumNextVals)

def partTwo():
    sumNextVals = 0
    for l in lines:
        highestVals = l.split()
        for i, t in enumerate(highestVals):
            highestVals[i] = int(t)


        allZeros = False
        listList = [] # keep track of hierarchy of lists
        listList.append(highestVals)

        parentVals = highestVals
        childVals = []
        while not allZeros:
            i = 1
            while i < len(parentVals):
                childVals.append(parentVals[i] - parentVals[i-1])
                i += 1
            listList.append(childVals)
                
            allZeros = True
            for v in childVals:
                if v != 0:
                    allZeros = False
                    break

            if not allZeros:
                parentVals = childVals
                childVals = []

        # predict next value
        lowerVal = 0
        for i, l in enumerate(listList[::-1]):
            if i != 0:
                lowerVal = l[0] - lowerVal

        sumNextVals += lowerVal
        
    print(sumNextVals)


partTwo()
