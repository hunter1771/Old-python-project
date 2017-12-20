# Hunter hulsey
#Five dice

import random
#game loop
keep_going = True
while keep_going:
    #roll dice
    dice = [0,0,0,0,0]
    for i in range(5):
        dice[i] = random.randint(1,6)
    print("you rolled:", dice)
    #sort
    dice.sort()
    if dice[0] == dice[4]:
        print("Yahtzee!")

    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("four of a kind")

    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("three of a kind")
    keep_going = (input("Hit [enter] to keep going, and key to exit: ") == "")
    
#notes: appers to be bugged, only displays three of a kind in my tests
