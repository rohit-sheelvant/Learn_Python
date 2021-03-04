num = int(input('enter the number:'))
if num!=0:
    if (num % 2) == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
else:
    print('0 is either even or odd')