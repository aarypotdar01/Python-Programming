student = {
    "name" : "Aary",
    "age" : 21,
    "branch" : "ENTC",
    "college" : "KIT"
}

key = input("Enter a key to search: ")

if key in student:
    print("Key exist!")
    print("Value =", student[key])
else:
    print("Key doesn't exist!")