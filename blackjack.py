#All code is my own, no provided code or hints were used.
#Idea to do project from Angela Yu
#NOTE: I acknowledge that there is no split, double down, or wager methods implemented. I wanted this just to be the base blackjack.

import random

#Function to create the deck
def makeDeck():
    deck = []
    #Add all of the possible number cards to the list
    for x in range(1, 11):
        deck.append(str(x))

    #Add all face cards
    deck.extend(["A", "K", "J", "Q"])

    #Return the deck multiplied by 4 in order to match a full deck
    return deck * 4

#Create a variable that holds a made deck
initDeck = makeDeck()

#Reset deck if it is empty (IF THE SHUFFLE OCCURS IN THE MIDDLE OF THE ROUND THE ODDS WILL BE WRONG)
def checkDeck(dict):
    if(len(dict["deck"]) == 0):
        dict["deck"] = initDeck
    return dict

#Give cards to a person within the dict
def giveCard(person, dict):
    dict = checkDeck(dict)
    #Card is the index of the card from the deck
    card = random.randint(0, len(dict["deck"]) - 1)
    #Add card to string
    dict[person] = dict[person] + str(f"{dict["deck"][card]}") + "|"
    dict["deck"].pop(card) 
    return dict

#Make the hands at the start of the round
def makeHands(dict):
    #giveCard only gives a singular card at a time
    dict = giveCard("playerHand", dict)
    dict = giveCard("playerHand", dict)
    dict = giveCard("dealerHand", dict)
    dict = giveCard("dealerHand", dict)
    return dict   

#Checks if someone has busted or has blackjack
def checkCards(dict):
    #Dealer busts
    if (dict["dealerScore"] > 21):
        print("Dealer Busts!\n")
        return
    #Dealer and player have the same score
    elif (dict["dealerScore"] == dict["playerScore"]):
        print("Push!\n")
        return
    #Dealer has a better hand
    elif (dict["dealerScore"] >= dict["playerScore"]):
        print("Dealer Wins!")
        return
    #You have the better hand
    else:
        print("You Win!")
        return

#Check if the player has busted
def checkPlayer(dict):
    if(dict["playerScore"] > 21):
        print("You Bust!")
        return True
    else:
        return False

#Call the function to update both scores
def bothScores(dict):
    dict = updateScore("playerScore", "playerHand", dict)   
    dict = updateScore("dealerScore", "dealerHand", dict)
    return dict       

#Update the score of a person
def updateScore(person, personHand, dict):
    hand = dict[personHand]
    score = 0
    hasAce = 0
    
    #For the amount of cards in the hand, match the value
    for x in range (0, len(hand)):
        match hand[x]:
            case "A":
                if (score + 11 > 21):
                    score += 1
                else:
                    score += 11
                    hasAce += 1
            case "K" | "Q" | "J":
                score += 10
            case "0":
                score += 9
            case "|":
                continue
            case _:
                score += int(hand[x])
    
    #If they bust but have an ace counting as 11
    if(score > 21 and hasAce):
        score - 10

    dict[person] = score
    return dict

#Show the cards but only one for the dealer
def firstDisplay(dict):
    print(f"The dealer has {dict["dealerHand"][0]}")
    print(f"The player has {dict["playerHand"]}({dict["playerScore"]})")

#Print the hands and score
def displayHands(dict):
    print(f"The dealer has {dict["dealerHand"]}({dict["dealerScore"]})")
    print(f"The player has {dict["playerHand"]}({dict["playerScore"]})")
    return
    
#Check if either person has blackjack
def checkBlackJack(dict):
    if (dict["playerScore"] == 21 and dict["dealerScore"] == 21):
        print("Both have BlackJack!\n Push!")
        playGame = input("play or exit\n")
        return 1
    elif(dict["playerScore"] == 21):
        print("BlackJack!")
        playGame = input("play or exit\n")
        return 1
    elif(dict["dealerScore"] == 21):
        print("Dealer has Blackjack!")
        playGame = input("play or exit\n")
        return 1
    else:
        return 0

#Ask the user if they would like to hit
def askHit(dict):
    while(True):
        answer = input("Would you like to hit? (type hit or hold)\n")
        if (answer == "hit"):
            dict = giveCard("playerHand", dict)
            dict = updateScore("playerScore", "playerHand", dict)
            firstDisplay(dict)
            if(dict["playerScore"] == 21):
                return dict
            if (checkPlayer(dict)):
                dict["gameOver"] = 1
                return dict
        else:
            return dict
    
#Reset all of the hands and scores
def clearHands(dict):
    dict["playerScore"] = 0
    dict["playerHand"] = ""
    dict["dealerScore"] = 0
    dict["dealerHand"] = ""
    dict["gameOver"] = 0
    return dict

def main():
    #The player initially starts with 100 credits
    tableDict = {
        "playerHand" : "",
        "playerScore" : "",
        "dealerHand" : "",
        "dealerScore" : 0,
        "deck" : initDeck,
        "account" : 100,
        "wager" : 0,
        "gameOver" : 0
}
    
    #Ask the user for what they want to do
    playGame = input("Enter play or exit\n")

    #While the user doesn't exit
    while (playGame != "exit"):

        #Create hands, update score, then display score. Then check if either hand has blackjack.
        tableDict = makeHands(tableDict)
        tableDict = bothScores(tableDict)
        firstDisplay(tableDict)
        if (checkBlackJack(tableDict)):
            tableDict = clearHands(tableDict)
            continue

        #If askHit is true, that means the player busted, if it breaks, the player decided to hold
        tableDict = askHit(tableDict)
        if(tableDict["gameOver"]):
            tableDict = clearHands(tableDict)
            playGame = input("play or exit\n")
            continue

        displayHands(tableDict)

        #While the dealer is under 17, they will continue to hit.
        while(tableDict["dealerScore"] < 17):
            tableDict = giveCard("dealerHand", tableDict)
            tableDict = bothScores(tableDict)
            print("")
            displayHands(tableDict)

        #Check who won then clear hands.
        checkCards(tableDict)
        tableDict = clearHands(tableDict)
        playGame = input("play or exit\n")
        

main()
