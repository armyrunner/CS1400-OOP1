
# Yahtzee:

""" The program Yahtzee is to calculate the roll of 5 dice and to roll it one million times.  I will also
write the mathematical problem to check it against the rolls of dice and see how close you get."""

# proggrammer: Andrew Nelson
# Intial Coding 10/06/18

# IMPORTS TO USE IN THE PROGRAM
import random

def main():

    # Print Instructions
    print("")
    print("This function will simulate rolling 5 dice tat least one million times. It \n"
          "will keep track of the number of times the computer rolls a Yahtzee. The \n"
          "function will return the number or wins divided by the number of tries. ")
    print(" ")
    print(" ")

    ycount = int(input("How many do you want to run the simulation? ->"))
    print("")

    # The values of the math problem of the dice

    print("The mathematical solution is: ",mathSolution())

    yahttotal = 0


    for i in range(10):

        yahttotal += Yahtzee_Simulation(ycount)
        
    return print("The simulation solution is:", yahttotal/ycount)


def mathSolution():

    total1 = 6/6 * (1/6 **4)

    return float(total1)


def Yahtzee_Simulation(ycount):

    yahtzeecount = 0

    for i in range(ycount):

        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)
        dice5 = random.randrange(1,7)

        if dice1 == dice2 == dice3 == dice4 == dice5:
            yahtzeecount += 1    

    return yahtzeecount

main()
