'''
Exercise 1 - Printing

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
'''

'''
Printing multiple lines
print("Hello world!\nHello world!\nHello world!")
'''

# input() will get the user input in console, then print de word hello and the user input
# print("Hello " + input("What is your name?"))

# Exercise 3 -
my_string = input("What is your name? ")
print(len(my_string))

# Exercise 4
a = input("a: ")
b = input("b: ")

aux = a
a = b
b = aux

print("a: " + a)
print("b: " + b)

# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line:

print("Welcome to the Band Name Generator")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is: " + city + " " + pet)
