import numpy as np

lines = open('C:/Users/Nick Albright/Projects/AdventOfCode2023/Day7/input.txt', 'r').read().splitlines()
cardValueMap = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}

def partOne():
    handAndBid = []
    for l in lines:
        hand, bid = l.split()
        handAndBid.append((hand, int(bid)))


    handAndBid.sort(key=lambda handAndBid: strengthFunction(handAndBid[0]))
    
    winnings = 0
    for i in range(len(handAndBid)):
        winnings += (i + 1) * handAndBid[i][1]
    print(winnings)

def isFiveOfKind(cardsInHand):
    counts = cardsInHand.values()
    return 5 in counts

def isFourOfKind(cardsInHand):
    counts = cardsInHand.values()
    return 4 in counts

def isFullHouse(cardsInHand):
    counts = cardsInHand.values()
    return 3 in counts and 2 in counts

def isThreeOfKind(cardsInHand):
    counts = cardsInHand.values()
    return 3 in counts

def isTwoPair(cardsInHand):
    counts = cardsInHand.values()
    twoCounter = 0
    for c in counts:
        if c == 2:
            twoCounter += 1
            if twoCounter == 2:
                return True
    return False

def isOnePair(cardsInHand):
    counts = cardsInHand.values()
    return 2 in counts


def getHandValue(hand):
    cardsInHand = {}
    for card in hand:
        if card in cardsInHand:
            cardsInHand[card] += 1
        else:
            cardsInHand[card] = 1
    if isFiveOfKind(cardsInHand):
        return 7
    if isFourOfKind(cardsInHand):
        return 6
    if isFullHouse(cardsInHand):
        return 5
    if isThreeOfKind(cardsInHand):
        return 4
    if isTwoPair(cardsInHand):
        return 3
    if isOnePair(cardsInHand):
        return 2
    return 1

def strengthFunction(hand):
    val = getHandValue(hand), [cardValueMap.get(card, card) for card in hand]
    return val

############ P2 methods begin #####################

def partTwo():
    handAndBid = []
    for l in lines:
        hand, bid = l.split()
        handAndBid.append((hand, int(bid)))


    handAndBid.sort(key=lambda handAndBid: strengthFunctionP2(handAndBid[0]))    
    winnings = 0
    for i in range(len(handAndBid)):
        winnings += (i + 1) * handAndBid[i][1]
    print(winnings)

def getHandValueP2(hand):
    cardsInHand = {}
    numJokers = 0
    for card in hand:
        if card != 'J': # don't count jokers
            if card in cardsInHand:
                cardsInHand[card] += 1
            else:
                cardsInHand[card] = 1
        else: numJokers += 1
    if isFiveOfKindP2(cardsInHand, numJokers):
        return 7
    if isFourOfKindP2(cardsInHand, numJokers):
        return 6
    if isFullHouseP2(cardsInHand, numJokers):
        return 5
    if isThreeOfKindP2(cardsInHand, numJokers):
        return 4
    if isTwoPairP2(cardsInHand, numJokers):
        return 3
    if isOnePairP2(cardsInHand, numJokers):
        return 2
    return 1


def strengthFunctionP2(hand):
    val = getHandValueP2(hand), [cardValueMap.get(card, card) for card in hand]
    return val

def isFiveOfKindP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    max = 0
    for c in counts:
        if c > max:
            max = c
    return max + numJokers >= 5

def isFourOfKindP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    max = 0
    for c in counts:
        if c > max:
            max = c
    return max + numJokers >= 4

def isFullHouseP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    if numJokers == 0:
        return 3 in counts and 2 in counts
    twoCounter = 0
    for c in counts:
        if c == 2:
            twoCounter += 1
            if twoCounter == 2:
                return numJokers >= 1
    return False
    
def isThreeOfKindP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    max = 0
    for c in counts:
        if c > max:
            max = c
    return max + numJokers >= 3

def isTwoPairP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    twoCounter = 0
    for c in counts:
        if c == 2:
            twoCounter += 1
            if twoCounter == 2:
                return True
    if numJokers > 1:
        return True
    if 2 in counts and numJokers >= 1:
        return True
    return False

def isOnePairP2(cardsInHand, numJokers):
    counts = cardsInHand.values()
    return 2 in counts or numJokers >= 1

cardStrength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] # unused in correct solution
# This try got the sample and other users' test inputs, but not the real. I think it failed on small decimal approximation, so I had to go another way
def partOneFirstTry(): 
    hands = []
    handStrengths = []
    bids = []
    for i, l in enumerate(lines):
        hands.append(l.split(' ')[0])
        bids.append(int(l.split(' ')[1]))

        cardsInHand = {}
        for card in hands[i]:
            if card in cardsInHand:
                cardsInHand[card] += 1
            else:
                cardsInHand[card] = 1
        handStrength = 0
        if isFiveOfKind(cardsInHand):
            handStrength = 7
        elif isFourOfKind(cardsInHand):
            handStrength = 6
        elif isFullHouse(cardsInHand):
            handStrength = 5
        elif isThreeOfKind(cardsInHand):
            handStrength = 4
        elif isTwoPair(cardsInHand):
            handStrength = 3
        elif isOnePair(cardsInHand):
            handStrength = 2
        else:
            handStrength = 1

        handStrengths.append(handStrength)

    handArr = np.zeros((len(hands), 2))
    for i in range(len(handStrengths)):
        handArr[i][0] = i # index to track through sort
        handArr[i][1] = handStrengths[i]

    for i in range(len(handStrengths)):
        handArr[i][1]  = createHandValue(hands[i], handArr[i][1])

    sortedIndex = np.argsort(handArr[:, 1])
    handArr = handArr[sortedIndex]

    # determine answer with bids
    winnings = 0
    for i in range(len(handStrengths)):
        handIndex = int(handArr[i][0])
        bid = bids[handIndex]
        winning = (i + 1) * bid
        winnings += winning

    print(winnings)

# This failed due to small value approximation issues I think
def createHandValue(hand, handStrength):
    cardValue = 0 # tiebreaker using decimals
    multiplier = .1 # use this so subsequent cards are worth less
    for i in range(len(hand)):
        cardValue += (cardStrength.index(hand[i]) + 1) * multiplier
        multiplier /= (len(cardStrength) + 5)
    return cardValue + handStrength

def compareTiedHands(hand1, hand2):
    for i in range(len(hand1)): # compare card by card, THI SWONT WORK
        if cardStrength.index(hand1[i]) < cardStrength.index(hand2[i]):
            return 1
        elif cardStrength.index(hand1[i]) > cardStrength.index(hand2[i]):
            return 2


partTwo()