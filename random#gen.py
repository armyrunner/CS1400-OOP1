import random

def main():
    # print instructions
    print("Welcome to Mastermind. I have a numb from")
    print("1000 to 9999. You gues and I will tell you")
    print("how many digit are correct")

    #get a random number
    xnumb = random.randrange(1000,10000)
    xstr = str(xnumb)

    print(xstr)

    #give the user # of tries
    for i in range(20):
        print("Lucky Guess #",i+1)
        xget = input("    What is your lucky guess ->")
        kount = 0
        for i in range(len(xstr)):
            if xstr[i] == xget[i]:
                kount += 1
                print( " You got", kount,"correct")
            if kount == 4:
                print("YOU WON!!!")
                return
    print("Thanks for Playing")
    if kount != 4:
        print("You Lost HAHAH")
        print("The correct number was",xstr)
    else:
        print("You Won.")


main()
