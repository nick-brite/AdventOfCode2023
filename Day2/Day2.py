def partOne():
    lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day2/input.txt', 'r').read().splitlines()

    redVal = 12
    greenVal = 13
    blueVal = 14

    possibleGameSum = 0
    for i, l in enumerate(lines):
        eligibleGame = True

        rounds = l.split(';')
        rounds[0] = rounds[0].split(':')[1].strip() # trim game tracker
        for r in rounds:
            redCubesShown = 0
            greenCubesShown = 0
            blueCubesShown = 0

            item = r.split(',')
            for it in item:
                splitItem = it.strip().split(' ')
                cubeNum = int(splitItem[0])
                if splitItem[1] == "red":
                    redCubesShown += cubeNum
                elif splitItem[1] == "green":
                    greenCubesShown += cubeNum
                elif splitItem[1] == "blue":
                    blueCubesShown += cubeNum

            eligibleGame = redCubesShown <= redVal and greenCubesShown <= greenVal and blueCubesShown <= blueVal
            if not eligibleGame:
                break
        
        if eligibleGame:
            possibleGameSum += i + 1
        else: print("eligible game: " + str(i + 1))

    print(possibleGameSum)

def partTwo():
    lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day2/input.txt', 'r').read().splitlines()

    powerSum = 0
    for l in lines:
        maxRed = -1
        maxGreen = -1
        maxBlue = -1

        rounds = l.split(';')
        rounds[0] = rounds[0].split(':')[1].strip() # trim game tracker
        for r in rounds:
            redCubesShown = 0
            greenCubesShown = 0
            blueCubesShown = 0

            item = r.split(',')
            for it in item:
                splitItem = it.strip().split(' ')
                cubeNum = int(splitItem[0])
                if splitItem[1] == "red":
                    redCubesShown += cubeNum
                elif splitItem[1] == "green":
                    greenCubesShown += cubeNum
                elif splitItem[1] == "blue":
                    blueCubesShown += cubeNum

            if redCubesShown > maxRed:
                maxRed = redCubesShown
            if greenCubesShown > maxGreen:
                maxGreen = greenCubesShown
            if blueCubesShown > maxBlue:
                maxBlue = blueCubesShown

        powerSum += maxRed * maxGreen * maxBlue

    print(powerSum)

partTwo()