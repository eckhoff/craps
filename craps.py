import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

numbs = [2,3,4,5,6,7,8,9,10,11,12]
stats = [0,0,0,0,0,0,0,0,0,0,0]

def sort():
    if a == 2:
        stats[0] = stats[0] + 1
    if a == 3:
        stats[1] = stats[1] + 1
    if a == 4:
        stats[2] = stats[2] + 1
    if a == 5:
        stats[3] = stats[3] + 1
    if a == 6:
        stats[4] = stats[4] + 1
    if a == 7:
        stats[5] = stats[5] + 1
    if a == 8:
        stats[6] = stats[6] + 1
    if a == 9:
        stats[7] = stats[7] + 1
    if a == 10:
        stats[8] = stats[8] + 1
    if a == 11:
        stats[9] = stats[9] + 1
    if a == 12:
        stats[10] = stats[10] + 1

i = 0

while i < 20000:
    a = roll()
    sort()
    i = i + 1

y_pos = np.arange(len(stats))

plt.bar(y_pos, stats, align='center', alpha=0.5)
plt.xticks(y_pos, numbs)
plt.ylabel('frequency')
plt.title('likelyhood of 2 dice roll')

plt.show()
