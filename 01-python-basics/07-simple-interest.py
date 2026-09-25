principle = float(input("Enter the Principle amount: "))
rate = float(input("Enter the Interest rate: "))
time = float(input("Enter duration of investment in years: "))

simple_interest = (principle * rate * time) / 100

roi = simple_interest - principle 

print("Your Simple interest is:", simple_interest)

print("Your Return on investment is:", roi)