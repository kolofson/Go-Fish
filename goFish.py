import random

player1Hand = list()
player1Pairs = 0
player2Hand = list()
player2Pairs = 0
deck = [
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace"
]

def checkForPairs(hand):
    points = 0
    for card in hand:
        if hand.count(card) > 1:
            #Remove the pair
            hand.remove(card)
            hand.remove(card)
            points += 1
    return points

#Shuffle Deck of Cards
random.shuffle(deck)

print("\nWelcome to Go Fish!\n")

#Give Cards to Players
for i in range(5):
    card = deck.pop()
    player1Hand.append(card)
for i in range(5):
    card = deck.pop()
    player2Hand.append(card)

#Check for Duplicates
player1Pairs = checkForPairs(player1Hand)
player2Pairs = checkForPairs(player2Hand)

#Game Starts
while True:
    if len(player1Hand) < 1 or len(player2Hand) < 1:
        break
    while True:
        print("Your cards: " , player1Hand)
        wantedCard = input("What card do you wish for?\n")

        if wantedCard in player2Hand:
            print("Great Job!")
            player1Hand.remove(wantedCard)
            player2Hand.remove(wantedCard)
            player1Pairs += 1
            continue
        else:
            print("Go Fish!")
            player1Hand.append(deck.pop())
            break
        #Checks for Game End
        if len(player1Hand) < 1 or len(player2Hand) < 1:
            break
        
    #Check For Player 1 Pairs
    player1Pairs += checkForPairs(player1Hand)

    while True:
        #CPU Turn
        cardChoice = random.choice(player2Hand)
        print("Player 2 Asked for " + cardChoice)
        if cardChoice in player1Hand:
            player1Hand.remove(cardChoice)
            player2Hand.remove(cardChoice)
            player2Pairs += 1
            continue
        else:
            print("Player 2 had to go fishing!")
            player2Hand.append(deck.pop())
            break
        #Checks for Game End
        if len(player1Hand) < 1 or len(player2Hand) < 1:
            break
    #Check for Player 2 Pairs
    player2Pairs += checkForPairs(player2Hand)
#Game Ended
print("Game Over!\n\n" + "Scores: \n" + "\nPlayer 1: " , player1Pairs)
print("Player 2: " , player2Pairs)
