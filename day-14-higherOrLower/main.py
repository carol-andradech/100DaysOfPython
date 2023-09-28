from art import logo, vs
import random
from game_data import data

end = False
score = 0


def randomAccount():
    return random.choice(data)


def compareFollowers(optionA, optionB, answer):
    if answer == "A" and optionA['follower_count'] > optionB['follower_count']:
        return optionA
    elif answer == "B" and optionB['follower_count'] > optionA['follower_count']:
        return optionB
    else:
        return False


optionA = randomAccount()
while not end:

    optionB = randomAccount()

    print(logo)
    print(
        f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
    print(vs)
    print(
        f"Agaisnt B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")

    compare = compareFollowers(optionA, optionB, answer)

    if compare == False:
        print(f"Sorry, that's wrong. Final Score: {score}")
        end = True
    else:
        optionA = compare
        score += 1
        print(f"You're right! Current score: {score}")
