from art import logo
import random

print(logo)

end = False


def randomFunction():
    num = random.randint(0, 12)
    return num


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def printCards(cards, sum):
    print(f"Cartas:[", end=" ")
    for i, card in enumerate(cards):
        if i == len(cards) - 1:
            print(f"{card}", end=" ")
        else:
            print(f"{card},", end=" ")
    print(f"]. Pontuação: {sum}")


def verifyWin(sumPc, sumPlayer):

    if sumPlayer > 21 and sumPc > 21:
        return "You lose"

    if sumPlayer == sumPc:
        return "Draw"
    elif sumPc == 0:
        return "You lose. Pc wins"
    elif sumPlayer == 0:
        return "You win!"
    elif sumPlayer > 21:
        return "You went over. You lose"
    elif sumPc > 21:
        return "Opponent went over. You win"
    elif sumPlayer > sumPc:
        return "You win"
    else:
        return "You lose"


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = []
pcCards = []
playerCards.append(cards[randomFunction()])
playerCards.append(cards[randomFunction()])
pcCards.append(cards[randomFunction()])
pcCards.append(cards[randomFunction()])
sumPlayer = calculateScore(playerCards)
sumPc = calculateScore(pcCards)


while not end:
    print(f"Suas", end=" ")
    printCards(playerCards, sumPlayer)
    print(f"Carta do PC : [{pcCards[0]}]")

    if sumPlayer == 0 or sumPc == 0 or sumPlayer > 21:
        end = True
    else:
        hit = input("Digite 's' para continuar e 'n' para sair. ")
        if hit == "s":
            playerCards.append(cards[randomFunction()])
            sumPlayer = calculateScore(playerCards)
        else:
            end = True

while sumPc != 0 and sumPc < 17:
    print(f"Suas", end=" ")
    printCards(playerCards, sumPlayer)
    pcCards.append(cards[randomFunction()])
    sumPc = calculateScore(pcCards)
    print(f"Pc", end=" ")
    printCards(pcCards, sumPc)


print("-------------------------------------------------")
print(f"Sua mão final: {playerCards}, pontuação final: {sumPlayer}")
print(f"Mão final do PC: {pcCards}, pontuação final: {sumPc}")
print(verifyWin(sumPc, sumPlayer))
