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
        return craps, 2
    if total == 3:
        craps = 'craps'
        return craps, 3
    if total == 4:
        status = 'on'
        point = 4
        return status, point
    if total == 5:
        status = 'on'
        point = 5
        return status, point
    if total == 6:
        status = 'on'
        point = 6
        return status, point
    if total == 7:
        craps = 'win'
        return craps, 7
    if total == 8:
        status = 'on'
        point = 8
        return status, point
    if total == 9:
        status = 'on'
        point = 9
        return status, point
    if total == 10:
        status = 'on'
        point = 10
        return status, point
    if total == 11:
        craps = 'win'
        return craps, 11
    if total == 12:
        craps = 'craps'
        return craps, 12

# def roll_on():
total = roll()
print(roll_off())
# print(status)
# print(point)
# print(craps)
# print(total)
