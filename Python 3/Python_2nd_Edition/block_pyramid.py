'''
How tall will a pyramid wall be with x amount of blocks?
Malachi Campomizzi 10/24/2022
python 3.10.9
'''
def solution(x):
    if x == 1:
        print('Technically this is not a pyramid wall. . . ')
        return 1, 0
    elif x == 0:
        print('This program is of no use to you.')
        return None
    elif x < 0:
        print('How do you have negative blocks?')
        return None
    for i in range(1, x):
        if x >= 0:
            x -= i
        else:
            return i - 2, x + (i - 2) + 1

while True:
    try:
        pile = int(input('How many blocks do you have?\n--> '))
        answer = solution(pile)
        if answer != None:
            print(f'The height of the pyramid wall will be: {answer[0]}\nWith {answer[1]} blocks left over')
        break
    except:
        print('Enter a valid whole number !')
