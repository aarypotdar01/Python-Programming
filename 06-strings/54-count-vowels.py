text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("Vowels in string is/are:", count)