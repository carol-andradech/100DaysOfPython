height = int(input("Height of the wall: \n"))
width = int(input("Width of the wall: \n"))
coverage = 5


def paint(height, width, coverage):
    result = round((height*width)/coverage)
    print(f"You'll need {result} cans of paint.")


paint(height, width, coverage)
