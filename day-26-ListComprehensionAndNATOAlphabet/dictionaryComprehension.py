# new_dict = {new_key: new_value for item in list}
# We can also create a new dictionary based on the values in a existing dictionary
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# One step further, we can add our conditions at the very end
# new_dict = {new_key: new_value for ('key, value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1,100) for student in names}
# Use student_scores dictionary for my new dictionary

passed_students = {student:grade for (student,grade) in students_scores.items() if grade >= 60}
print(students_scores)
print(passed_students)

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Hint
# Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.
# You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.

# sentence = input("Write the phrase: ").split()
# print(sentence)
# result = {word:len(word) for word in sentence}
# print(result)

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.

# weather_c = eval(input())
weather_c = {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}
weather_f = {day:(temp * 9/5) + 32  for (day, temp) in weather_c.items()}
print(weather_f)

# How to iterate over a Padas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [90, 80, 70]
}
# Looping through dictionaries
for(key,value) in student_dict.items():
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for(key,value) in student_data_frame.items():
#     print(value)

print(("----------------"))
# Pandas have a inbult loop and it's a method called iterrows. Loop through row os a data frame rathen than columns
for(index, row) in student_data_frame.iterrows():
    print(row.score)
