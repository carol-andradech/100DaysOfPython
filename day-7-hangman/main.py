from hangman_words import word_list
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word = random.choice(word_list)
display = []
game_over = False
life = 6

for i in range(len(word)):
    display += "_"

print(f"{logo}")
print(f"{display}")


while not game_over:
    guess = input("Choose a letter to make a guess:\n").lower()

    for x in range(len(word)):
        letter = word[x]
        if letter == guess:
            display[x] = letter

    if guess not in word:
        print(f"You are wrong.")
        print(f"{stages[life]}")
        life -= 1

    print(f"{' '.join(display)}")

    if life == -1:
        game_over = True
        print(f"Game Over")
        print(f"The word was: {word}")

    if "_" not in display:
        game_over = True
        print("You won")
