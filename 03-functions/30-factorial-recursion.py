def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial doesn't exit for negative number")
else:
    result = factorial(num)
    print("Factorial =", result)