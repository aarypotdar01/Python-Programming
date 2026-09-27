def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        next_num = a + b
        a = b
        b = next_num

num = int(input("Enter a number:"))

if num <= 0:
    print("Please enter a positive number!")
else:
    fibonacci(num)


