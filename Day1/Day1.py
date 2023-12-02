
def partOne():
    lines = open('input.txt', 'r').read().splitlines()

    calSum = 0
    for l in lines:
        # forwards to get first digit
        for c in l:
            if c.isdigit():
                calSum += int(c) * 10
                break

        # backwards to get last digit
        for c in reversed(l):
            if c.isdigit():
                calSum += int(c)
                break

    print("total calories: " + str(calSum))


def partTwo():
    lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day1/input.txt', 'r').read().splitlines()
    # now we have to search for words, both forwards and backwards
    numberWords = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    reversedNumberWords = {key[::-1]: value for key, value in numberWords.items()}

    calSum = 0
    for l in lines:
        # forwards to get first digit
        for i, c in enumerate(l):
            foundDigit = -1
            if i < 6:
                foundDigit = translateSubstringToDigit(l[:i], numberWords)
            else:
                # 5 for longest word, eight. Also at this length, no two words can overlap
                foundDigit = translateSubstringToDigit(l[i-5:i], numberWords)
            if foundDigit != -1:
                calSum += foundDigit * 10
                break

            # if no number word was found, check for digit
            if c.isdigit():
                calSum += int(c) * 10
                break


        # flip string backwards
        reversed_line = l[::-1]
        for i, c in enumerate(reversed_line):
            foundDigit = -1
            if i < 6:
                foundDigit = translateSubstringToDigit(reversed_line[:i], reversedNumberWords)
            else:
                # 5 for longest word, eight. Also at this length, no two words can overlap
                foundDigit = translateSubstringToDigit(reversed_line[i-5:i], reversedNumberWords)
            if foundDigit != -1:
                calSum += foundDigit
                break

            # if no number word was found, check for digit
            if c.isdigit():
                calSum += int(c)
                break

    print("total calories: " + str(calSum))


def translateSubstringToDigit(string, digitMap):
    for key in digitMap:
        if (key in string):
            return digitMap[key]
    return -1

partTwo()