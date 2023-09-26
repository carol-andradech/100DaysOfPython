import random

end = False
num = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficult == 'easy':
    lives = 10
elif difficult == 'hard':
    lives = 5


def verify(num, guess):
    if guess < num:
        print("Too Low.")
        return False
    elif guess > num:
        print("Too High.")
        return False
    elif guess == num:
        print("You guessed.")
        return True


while not end:
    guess = int(
        input(f"\nYou have {lives} attempts remaining. Guess a number: "))
    finished = verify(num, guess)
    lives -= 1
    if lives == 0:
        print(f"No more lives. You lost. The answer is: {num}")
        end = True
    elif finished:
        end = True
