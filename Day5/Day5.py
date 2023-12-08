from functools import reduce
import matplotlib.pyplot as plt

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day5/input.txt', 'r').read().splitlines()

def partOne():
    times = [x for x in lines[0].split(' ') if x.split()][1:]
    distances = [x for x in lines[1].split(' ') if x.split()][1:]

    answer = 1
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        successSum = 0

        for x in range(time):
            if x * (time - x) > distance:
                successSum += 1
        
        print(successSum)
        answer *= successSum
    print(answer)

def partTwo():
    time = int(lines[0].replace(" ", "").split(":")[1])
    distance = int(lines[1].replace(" ", "").split(":")[1])

    successSum = 0

    for x in range(time):
        if x * (time - x) > distance:
            successSum += 1
    
    print(successSum)
    
    
partTwo()
