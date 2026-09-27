def find_largest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = find_largest(num1, num2)

print("Result is:", result)