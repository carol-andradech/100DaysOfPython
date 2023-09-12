"""
height = int(input("Height of the wall: \n"))
width = int(input("Width of the wall: \n"))
coverage = 5


def paint(height, width, coverage):
    result = round((height*width)/coverage)
    print(f"You'll need {result} cans of paint.")


paint(height, width, coverage)



def prime_checker(number):
    count = 0
    for i in range(1, number+11):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    if count > 2:
        print("Not prime number")


n = int(input("Check this number:"))
prime_checker(number=n)


"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end = False


def encrypt_decode(text, shift, direction):
    result = ""

    if direction == "decode":
        shift *= -1
    # letter is a character of the text
    for letter in text:
        place = alphabet.index(letter)
        new_place = place + shift
        result += alphabet[new_place]

    print(f"{result}")


while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt_decode(text, shift, direction)
    if (end == False):
        end_update = input(
            "Type 'yes' if you want to go again. Otherwise type 'no': ")
        if end_update == "yes":
            end = False
        else:
            end = True
