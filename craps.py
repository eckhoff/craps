import random

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

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

def roll_on():
    if point == total:
        status = 'off'
        return 'win', status
    elif total == 7:
        status = 'off'
        return 'loss', status
    else:
        status = 'on'
        return 'nothing yet', status

total = roll()
status = roll_off()[2]
win = roll_off()[0]
point = roll_off()[1]

while status == 'on':
    total = roll()
    status = roll_on()[1]
    win = roll_on()[0]

if win == 'win' and point != 'no point':
    print(win)
    print('the winning point was: ', total)
if win == 'loss' and point > 0:
    print(win)
    print('sorry, you sevened out')
    print('the point was: ', point)
if win == 'win' and point == 'no point':
    print('opening roll win!')
    print('you rolled a: ', total)
if win == 'craps':
    print(win)
    print('you crapped out with a: ', total)

