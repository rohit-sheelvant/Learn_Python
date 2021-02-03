# Program to calculate the number of Days, weeks and months from your current age till 90th age

age = input("What is your current age?")

age1 = int(age)
val = (90 - age1)
days = (val * 365)
weeks = (val * 52)
months = (val * 12)
print(f"You have {days} days, {weeks} weeks, {months} months left.")








