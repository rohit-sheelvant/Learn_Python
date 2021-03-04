# To find the multiplication table of a Given numbr
num = int(input('Enter a number for multiplication number of:'))
for i in range(1, 11):
    val = num * i
    print(f'{num} X {i} = {val}')