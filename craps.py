import random

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

numbs = [2,3,4,5,6,7,8,9,10,11,12]
stats = [0,0,0,0,0,0,0,0,0,0,0]
status = 'off'
point = 0
craps = 'nothing yet'

def roll_off():
    if total == 2:
        craps = 'craps'
        return craps, 'no point', 'off'
    if total == 3:
        craps = 'craps'
        return craps, 'no point', 'off'
    if total == 4:
        status = 'on'
        point = 4
        return 'nothing yet', point, status
    if total == 5:
        status = 'on'
        point = 5
        return 'nothing yet', point, status
    if total == 6:
        status = 'on'
        point = 6
        return 'nothing yet', point, status
    if total == 7:
        craps = 'win'
        return craps, 'no point', 'off'
    if total == 8:
        status = 'on'
        point = 8
        return 'nothing yet', point, status
    if total == 9:
        status = 'on'
        point = 9
        return 'nothing yet', point, status
    if total == 10:
        status = 'on'
        point = 10
        return 'nothing yet', point, status
    if total == 11:
        craps = 'win'
        return craps, 'no point', 'off'
    if total == 12:
        craps = 'craps'
        return craps, 'no point', 'off'

# def roll_on():
total = roll()
status = roll_off()[2]
win = roll_off()[0]
point = roll_off()[1]
print('win/loss =', win)
print('point is:', status)
print('the roll was a:', total)
print('the point to hit is:', point)
