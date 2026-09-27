def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)

print("Power of the given number is:", result)