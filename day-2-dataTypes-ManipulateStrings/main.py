# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
'''
two_digit_number = input("Type a two digit number: ")

first = int(two_digit_number[0])
second = int(two_digit_number[1])
sum = first + second

print("The result is: " + str(sum))
'''

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
'''
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_f = float(height)
weight_f = float(weight)

bmi = weight_f/(height_f*height_f)
bmi_i = int(bmi)
print(bmi_i)
'''

'''
# f-String
score = 0
height = 1.8
isWinning = True
print(
    f"your score is {score}, your height is {height}, you are winning is {isWinning}")
'''

'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
'''

age = input("How old are you?\n")

year = 90 - int(age)
months = round(year * 12)
weeks = round(year * 52)
days = round(year * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
