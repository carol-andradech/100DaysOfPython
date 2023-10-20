# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

#a for append. w for write.
#if a file doesn't exist, when you use w mode, it creates for you
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text")