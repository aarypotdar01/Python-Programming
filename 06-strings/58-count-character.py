text = input("Enter a string: ")
character = input("Enter the character to be counted: ")

count = 0

for char in text:
    if char == character:
        count = count + 1

print("Character occured", count, "time(s)")