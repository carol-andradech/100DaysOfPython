import random

'''
random_int = random.randint(1, 10)
print(random_int)

random_float = random.random() * 5
print(random_float)


coin = random.randint(0, 1)

if coin == 0:
    print("Heads")

else:
    print("Tails")
'''

'''
people = input("Type your names:\n")
people_list = people.split(", ")
print(people_list)
# random.choice(people_list)
paying = random.randint(0, len(people_list)-1)

print(paying)
print(f"{people_list[paying]}, is going to buy the meal today.")
'''

'''
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f'     {1}', f'    {2}', f'    {3}')
print(f"1 {row1}\n2 {row2}\n3 {row3}")

position = input("Where do you want to put the treasure?\n")
row = int(position[0])
column = int(position[1])
map[row-1][column-1] = "💰"

print(f"{row1}\n{row2}\n{row3}")
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____) 
---.__(___)
'''

game_images = [rock, paper, scissors]
player = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print(game_images[player])

pc = random.randint(0, 2)
print("Computer chose:\n")
print(game_images[pc])


if player == pc:
    print("Draw")
elif player == 0 and pc == 1:
    print("You Lose")
elif player == 0 and pc == 2:
    print("You win")
elif player == 1 and pc == 0:
    print("You win")
elif player == 1 and pc == 2:
    print("You Lose")
elif player == 2 and pc == 0:
    print("You Lose")
elif player == 2 and pc == 1:
    print("You Win")
