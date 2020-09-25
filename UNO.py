##Had to rush the last parts because I spent too long on this so the turn system and skip function are kind of sloppy(BUT THEY WORK!!!!!) :P
##This is only 250 points? You can do six 100 point challenges in the time it takes to do this D:
##This has to be easier using OOP right??

##Btw checking the wikipedia page for uno show a lot of weird rules(like you can only play draw four when you have no other option) that I never knew about but I can't bother with it.
##I also didn't add card chaining function(it doesn't even seem to be an actual rule, only applicable to draw fours) and reverse card function(there are only 2 players).

import random

cardSign = 0
cardColour = 1

##Used to create the distribution of different signs being generated.
cardPopulation = []

signs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "skip", "reverse", "draw_two", "0", "wild", "draw_four"]
colours = ["RED", "YELLOW", "GREEN", "BLUE", "ANY"]

cardPile = [[], []]
playerDeck = [[], []]
computerDeck = [[], []]

##Generate card population.
##Wild and plus four cards are twice as rare as other cards.
for i in range (0, 12):
    cardPopulation.append(signs[i])
    cardPopulation.append(signs[i])

for i in range(12, 15):
    cardPopulation.append(signs[i])

def DrawCard(targetDeck, isCardPile):
    if isCardPile:
        _sign = cardPopulation[random.randint(0, len(cardPopulation) - 3)]
    else:
      _sign = cardPopulation[random.randint(0, len(cardPopulation) - 1)]
    
    _colour = ""
    if IsSpecial(_sign) != True:
        _colour = colours[random.randint(0,3)]
    else:
        _colour = colours[-1]

    targetDeck[cardSign].append(_sign)
    targetDeck[cardColour].append(_colour)

def PlayCard(targetDeck, cardIndex, isPlayer):
    if isPlayer != True:
        print(f">Computer plays {CardString(targetDeck, cardIndex)}.")
        print()
    ##Replace card sign.
    cardPile[cardSign][0] = targetDeck[cardSign][cardIndex]
    ##Replace card colour.
    colourChoice = -1
    if targetDeck[cardColour][cardIndex] != colours[-1]:
        colourChoice = targetDeck[cardColour][cardIndex]
    elif isPlayer:
        while VerifyChoice(len(colours) - 1, colourChoice) != True:
            colourChoice = int(input("Choose colour(0 for red, 1 for yellow, 2 = green, 3 = blue) : "))
            print()
        colourChoice = colours[colourChoice]
    else:
        colourChoice = MostCommonColour(targetDeck)

    cardPile[cardColour][0] = colourChoice

    ##Remove card from deck
    targetDeck[cardSign].pop(cardIndex)
    targetDeck[cardColour].pop(cardIndex)

    ##Skip
    if cardPile[cardSign][0] == signs[9]:
        Skip(isPlayer)
    ##Draw Two
    if cardPile[cardSign][0] == signs[11]:
        DrawMultipleCards(isPlayer, 2)
    ##Draw Four
    if cardPile[cardSign][0] == signs[14]:
        DrawMultipleCards(isPlayer, 4)

def Skip(isPlayer):
    if isPlayer:
        nextTurn[0] = 0
        print(f">Computer's turn has been skipped.")
    else:
        nextTurn[0] = 1
        print(f">Player's turn has been skipped.")
            
def DrawMultipleCards(isPlayer, drawAmount):
    targetDeck = str()
    if isPlayer:
        targetDeck = computerDeck
        print(f">Computer draws {drawAmount} cards.")
    else:
        print(f">Player draws {drawAmount} cards.")
        targetDeck = playerDeck
    print()

    for i in range(0, drawAmount):
        DrawCard(targetDeck, False)

def IsSpecial(_sign):
    if _sign == signs[-1] or _sign == signs[-2]:
        return True

def VerifyPlacement(_sign, _colour):
    if _sign == cardPile[cardSign][0] or _colour == cardPile[cardColour][0] or _colour == colours[-1]:
        return True

def VerifyChoice(length, index):
    if index >= 0 and index < length:
        return True

def MostCommonColour(targetDeck):
    mostCommonColour = ""
    mostCommonColourCount = 0

    for i in range(0, len(colours) - 1):
        currentColour = colours[i]
        currentColourCount = 0
        for i in targetDeck[cardColour]:
            if i == currentColour:
                currentColourCount += 1
        if currentColourCount > mostCommonColourCount:
            mostCommonColour = currentColour
            mostCommonColourCount = currentColourCount

    return mostCommonColour

def PlayableCards(targetDeck):
    _playableCards = []
    for i in range(0, len(targetDeck[0])):
        if VerifyPlacement(targetDeck[cardSign][i], targetDeck[cardColour][i]) == True:
            _playableCards.append(i)
    return _playableCards

def CardString(targetDeck, cardIndex):
    return (f"[{targetDeck[cardSign][cardIndex]} {targetDeck[cardColour][cardIndex]}]")

def CardInputsString(_playableCards):
    out = "Choose card to play( "
    count = 0
    for i in _playableCards:
        out += f"{str(count)} for [{playerDeck[cardSign][i]} {playerDeck[cardColour][i]}], "
        count += 1
    return out[0:-2] + " ) : "

def PlayerMove():
    playableCards = PlayableCards(playerDeck)
             
    if len(playableCards) >= 1:
        choice = -1
        while VerifyChoice(len(playableCards), choice) != True:
            choice = int(input(CardInputsString(playableCards)))
            print()
        PlayCard(playerDeck, playableCards[choice], True)
    else:
        print(">No matches, player draws 1 card.")
        print()
        DrawCard(playerDeck, False)

def ComputerMove():
    playableCards = PlayableCards(computerDeck)
    
    if len(playableCards) >= 1:
        PlayCard(computerDeck, playableCards[random.randint(0, (len(playableCards) - 1))], False)
    else:
        print(">No matches, computer draws 1 card.")
        print()
        DrawCard(computerDeck, False)
    input("ENTER to continue : ")

def PrintCardPile():
    print("##Card Pile")
    print(CardString(cardPile, 0))
    print()

def PrintPlayerDeck():
    print(f"##Player Deck ({len(playerDeck[cardSign])} cards)")
    for i in range(0, len(playerDeck[cardSign])):
        print(CardString(playerDeck, i))
    print()

def PrintComputerDeck(hidden):
    print(f"##Computer Deck ({len(computerDeck[cardSign])} cards)")
    if hidden != True:
        for i in range(0, len(computerDeck[cardSign])):
            print(CardString(computerDeck, i))
    print()

DrawCard(cardPile, True)
for i in range (0, 7):
    DrawCard(playerDeck, False)
for i in range (0, 7):
    DrawCard(computerDeck, False)

print(cardPile)
print(playerDeck)
print(computerDeck)
print()

nextTurn = [0]
count = 1

while len(playerDeck[cardSign]) >= 1 and len(computerDeck[cardSign]) >= 1:
    print(f"Turn {count}")
    PrintCardPile()
    PrintPlayerDeck()
    PrintComputerDeck(True)
    if nextTurn[0] == 0:
        nextTurn[0] = 1
        PlayerMove()
    elif nextTurn[0] == 1:
        nextTurn[0] = 0
        ComputerMove()
    if len(playerDeck[cardSign]) == 1 or len(computerDeck[cardSign]) == 1:
        print(">UNO!")
        print()
    print()
    count += 1

if len(playerDeck[cardSign]) < len(computerDeck[cardSign]):
    print("PLAYER WINS!")
else:
    print("COMPUTER WINS!")