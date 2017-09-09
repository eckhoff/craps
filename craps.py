# Assumes $1000 bankroll with a $10 passline bet
# $10 odds on 4 and 10
# $20 odds on 5 and 9
# $30 odd on 6 and 8

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
        craps = 'offwin'
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
        craps = 'offwin'
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

def odds():
    if point == 4 or point == 10:
        odds = 2
        bet = 10
        return odds, bet
    if point == 5 or point == 9:
        odds = 3/2
        bet = 20
        return odds, bet
    if point == 6 or point == 8:
        odds = 6/5
        bet = 30
        return odds, bet

bankroll = 1000
pointhit = 0
pointmiss = 0
openwin = 0
openloss = 0
i = 0
while i < 10000:
    total = roll()
    status = roll_off()[2]
    win = roll_off()[0]
    point = roll_off()[1]


    while status == 'on':
        total = roll()
        status = roll_on()[1]
        win = roll_on()[0]

    if win == 'win':
        bankroll = bankroll + 10 + odds()[1]*odds()[0]
        pointhit = pointhit + 1
        i = i + 1
    if win == 'loss':
        bankroll = bankroll - 10 - odds()[1]
        pointmiss = pointmiss + 1
        i = i + 1
    if win == 'offwin':
        bankroll = bankroll + 10
        openwin = openwin + 1
        i = i + 1
    if win == 'craps':
        bankroll = bankroll - 10
        openloss = openloss + 1
        i = i + 1

print(bankroll)
print('you hit', pointhit, 'points')
print('you missed', pointmiss, 'points')
print('on the opening roll you won', openwin, 'times')
print('on the opening roll you lost', openloss, 'times')


