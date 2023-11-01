# Whats is a list comprehension? It's a case where you create a new list from a previous list.
# new_list = [new_item for item in list]

# Usign a for loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Carol"
# new_list = [letter for letter in name]
letters_list = [letter for letter in name]
# ['C', 'a', 'r', 'o', 'l']
print(letters_list)

#take a range (1,5), remember that it goes from 1,2,3,4
#loop through this range and then create a list where each of the number in the range is doubled [2,4,6,8]
my_range = range(1, 5)
# new_range = [n * 2 for n in my_range]
new_range = [n * 2 for n in range(1, 5)]
print(new_range)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Carol"]
# I only want the short name, names with four letters or less
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Challenge: Take the name with 5 letters or nome and turn each of these name to the uppercase version
upper_names = [n.upper() for n in names if len(n) >= 5]
print(upper_names)

# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
# First, use list comprehension to convert the list_of_strings to a list of integers.
# Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.
list_of_strings = input().split(',')
# TODO: Use list comprehension to convert the strings to integers 👇:
int_list = [int(n)for n in list_of_strings]
print(int_list)
# TODO: Use list comprehension to filter out the odd numbers
result = [n for n in int_list if n % 2 == 0]
# and store the even numbers in a list called "result"
print(result)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained:
#
# 1
# 2
# 3
# and file2.txt contained:
#
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.
# Hint
# Use the keyword method for starting the List comprehension and fill in the relevant parts.
#
# First, you will need to read from the files and create a list using the lines in the files.
#
# This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
#
# Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp
#
# Remember you can use the int() method in python to convert a string into an integer.


with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result_f = [int(num) for num in list1 if num in list2]
print(result_f)
