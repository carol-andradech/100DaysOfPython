"""
students_heights = [180, 124, 165, 173, 189, 169, 146]
i = 0
total = 0

for item in students_heights:
    total += item
    i += 1

media = round(total/i)

print(f"{media}")
"""

"""
students_scores = [78, 65, 89, 86, 55, 91, 64, 89]
max = 0

for item in students_scores:
    if item > max:
        max = item

print(f"The highest score in the class is: {max}")
"""

# for number in range (1,11,3):
#   print(number)

"""
total = 0
for number in range(2, 101, 2):
    total += number

print(f"{total}")
"""

"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


password = ""

# easy
for number in range(1, nr_letters+1):
    seed = random.randint(0, len(letters)-1)
    password += letters[seed]

for number in range(1, nr_numbers+1):
    seed = random.randint(0, len(numbers)-1)
    password += numbers[seed]

for number in range(1, nr_symbols+1):
    seed = random.randint(0, len(symbols)-1)
    password += symbols[seed]

print(f"{password}")

# hard
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print(f"Hard password:{final_password}")
