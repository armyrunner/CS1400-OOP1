# Roll Dice

# Initial Coding
# Andrew Nelson

import random

def main():

    keepGoing = True
    kount = 0
    while kount < 10:
        roll = dice(6)
        print(roll)
        
        if roll ==  6:
            break
        kount += 1
    print("I rolled a six")
        

def dice(sides):
    return random.randrange(1,sides+1)




main()
