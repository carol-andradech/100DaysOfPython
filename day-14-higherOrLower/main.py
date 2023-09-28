from art import logo, vs
import random
from game_data import data

end = False
score = 0


def randomAccount():
    return random.choice(data)


def compareFollowers(optionA, optionB, answer):
    if answer == "a" and optionA['follower_count'] > optionB['follower_count']:
        return True
    elif answer == "b" and optionB['follower_count'] > optionA['follower_count']:
        return True
    else:
        return False


print(logo)
optionA = randomAccount()
optionB = optionA
while not end:
    while optionB == optionA:
        optionB = randomAccount()
        print(optionB)

    print(
        f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
    print(vs)
    print(
        f"Agaisnt B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
    print(optionA['follower_count'])
    print(optionB['follower_count'])
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    compare = compareFollowers(optionA, optionB, answer)

    if compare == False:
        print(f"Sorry, that's wrong. Final Score: {score}")
        end = True
    else:
        print("\x1b[2J\x1b[H")
        optionA = optionB
        score += 1
        print(f"You're right! Current score: {score}")
