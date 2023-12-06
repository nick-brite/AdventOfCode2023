from functools import reduce
import matplotlib.pyplot as plt

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day5/input.txt', 'r').read().splitlines()

def partOne():
    seeds = lines[0].split(':')[1].strip().split(' ')
    seeds = list(map(int, seeds))
    locationNumbers = []
    for seed in seeds:
        print("seed: " + str(seed))
        seed = findNextThing(seed, lines.index("seed-to-soil map:"))
        seed = findNextThing(seed, lines.index("soil-to-fertilizer map:"))
        seed = findNextThing(seed, lines.index("fertilizer-to-water map:"))
        seed = findNextThing(seed, lines.index("water-to-light map:"))
        seed = findNextThing(seed, lines.index("light-to-temperature map:"))
        seed = findNextThing(seed, lines.index("temperature-to-humidity map:"))
        seed = findNextThing(seed, lines.index("humidity-to-location map:"))
        locationNumbers.append(seed)
    
    print(min(locationNumbers))


def findNextThing(seed, startIndex):
    i = startIndex + 1
    while i < len(lines) and len(lines[i]) > 0:
        destStart, sourceStart, rangeVal = map(int, lines[i].split(' '))

        if seed >= sourceStart and seed <= (sourceStart + rangeVal):
            # can translate
            print("translated number: " + str(destStart + (seed - sourceStart)))
            return destStart + (seed - sourceStart)
        i += 1
    # no translation found, return seed number
    print("no translation number: " + str(seed))
    return seed

def partTwo():
    seeds = lines[0].split(':')[1].strip().split(' ')
    seeds = list(map(int, seeds))
    seedIntervals = []
    i = 0
    while i < len(seeds):
        seedIntervals.append((seeds[i], seeds[i] + seeds[i+1]))
        i += 2

    seedIntervals = updateIntervals(seedIntervals, lines.index("seed-to-soil map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("soil-to-fertilizer map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("fertilizer-to-water map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("water-to-light map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("light-to-temperature map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("temperature-to-humidity map:"))
    seedIntervals = updateIntervals(seedIntervals, lines.index("humidity-to-location map:"))

    print(min(seedIntervals, key=lambda x: x[0]))
    

def updateIntervals(seeds, startIndex):
    i = startIndex + 1
    rangeLines = []
    while i < len(lines) and len(lines[i]) > 0:
        rangeLines.append(list(map(int, lines[i].split())))
        i += 1

    newIntervals = []
    while len(seeds) > 0:
        thisInterval = seeds.pop()

        for destStart, sourceStart, rangeVal in rangeLines:
            sourceInterval = (sourceStart, sourceStart + rangeVal)

            intersect = calculateIntersection(thisInterval, sourceInterval)
            if intersect:
                newIntervals.append((intersect[0] - sourceStart + destStart, intersect[1] - sourceStart + destStart))
                if thisInterval[0] < intersect[0]: # create bottom non-intersect group
                    seeds.append((thisInterval[0], intersect[0]))
                if thisInterval[1] > intersect[1]: # create top non-intersect group
                    seeds.append((intersect[1], thisInterval[1]))
                break
        else: # if no break
            newIntervals.append(thisInterval)

    seeds = newIntervals   
    return seeds            

def calculateIntersection(range1, range2):
    # Calculate the intersection
    interStart = max(range1[0], range2[0])
    interEnd = min(range1[1], range2[1])
    if interStart < interEnd:
        return (interStart, interEnd)
    return None

    
partTwo()

# This one was quite hard - I can't believe it's only Day 5. 
# I re-wrote my solution 3x, finally ending up with this stack-based method.
# An earlier array-based method was literally 1 value off (on an answer in the millions)
# 4 hours (and much googling) later, I shaved off that extra number, and got it