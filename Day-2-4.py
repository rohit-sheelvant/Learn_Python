# Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("what was the total bill?: $"))
tip = int(input("What percentage tip you like to give? 5, 9, 15, 19?: "))
person = int(input("How many people to split the bill?: "))
total = (bill + (bill * tip) / 100)
split_amount = total / person
total_amount = round(split_amount, 2)
print(f"Each person should pay: ${total_amount}")