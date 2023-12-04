lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day4/input.txt', 'r').read().splitlines()

def partOne():
    points = 0
    for l in lines:
        splitLine = l.strip().split('|')
        winningNumbers = splitLine[0].split(':')[1].strip().split(' ')
        myNumbers = splitLine[1].strip().split(' ')

        winningNumbers = list(filter(lambda x: x != "", winningNumbers))
        myNumbers = list(filter(lambda x: x != "", myNumbers))

        numWins = 0
        for item in winningNumbers:
            if item in myNumbers:
                numWins += 1
        
        if numWins != 0:
            roundPoints = 1
            for i in range(0, numWins - 1):
                roundPoints = roundPoints * 2
            points += roundPoints

    print(points)

def partTwo():
    lineWins = list(range(len(lines)))
    lineCopies = list(range(len(lines)))

    for i, l in enumerate(lines):
        splitLine = l.strip().split('|')
        winningNumbers = splitLine[0].split(':')[1].strip().split(' ')
        myNumbers = splitLine[1].strip().split(' ')

        winningNumbers = list(filter(lambda x: x != "", winningNumbers))
        myNumbers = list(filter(lambda x: x != "", myNumbers))

        numWins = 0
        for item in winningNumbers:
            if item in myNumbers:
                numWins += 1
        
        lineWins[i] = numWins
        lineCopies[i] = 1

    for i, wins in enumerate(lineWins):
        cap = i + wins
        if cap >= len(lines): # prevent overflow
            cap = len(lines) - 1
        for w in range(0, lineCopies[i]):
            for j in range(i + 1, cap + 1):
                lineCopies[j] += 1

    print(sum(lineCopies))

partTwo()
