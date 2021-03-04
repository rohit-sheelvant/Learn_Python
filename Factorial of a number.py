num = int(input('enter the number: '))
fact = 1
if num < 0:
    print("sorry no factorial for negative number")
elif num == 0:
    print("the factorail of 0 is 1")
else :
    for i in range(1, num + 1):
        fact = fact * i
    print(f"the factorial of {num} is {fact}")

