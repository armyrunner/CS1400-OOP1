import random
g_player_list = []
g_playerPoints = []
g_player = 0

def main():

     points = instructions()
     print(" ")
     player = int(input("Enter number of players 2 to 6 -> "))
     print(" ")


     request_name(player)


     play_game(points)


def instructions():

    print(" ")

    print("")
    print("Welcome to the Game of Pigs. To win, be the first\n"
          "player with the most points at the the end of the game. The\n"
          "game ends when all rounds are complete or reaches\n"
          "the max number of points. This game requires 2 to 6 players.")
    print("")

    print("On each turn, you many roll the die as many times as you \n"
          "like to obtain more points. However if you roll a 1, your turn is\n"
          "over, and you do not obtain any points for that turn.\n")
    print(" ")
    points = input("The game will play until how many points -> ")

    return points

def request_name(player):

    for i in range(player):
        print("Player",i +1,"Name please", end = " ")
        name = input("-> ")
        greeting(name)
        g_playerPoints.append(0)
        g_player_list.append(name)


def greeting(name):
    print("Thank you for playing",name)

def dice(sides):
    return random.randrange(1,sides+1)

def player_turn(index,points):

    score = 0
    name = g_player_list[index]

    while True:

        roll = dice(6)
        print(name,"You rolled a ", roll)

        if roll != 1:

            score += roll

            print(name, "has", score)
            print(" ")

        if roll == 1:
            score = 0
            print("Your Turn is over next players turn")
            print(" ")
            print("======================================")
            print(" ")

            break
        elif roll_again() == "2":
            break


    return score

def play_game(points):

    points = int(points)

    while max(g_playerPoints) < points:


        for i in range(len(g_player_list)):
            print("It is "+g_player_list[i]+"'s turn")
            g_playerPoints[i] += player_turn(i,points)

            print(g_player_list[i],"Your Current Score is ", g_playerPoints[i])


    biggest = 0
    index = 0

    for i in range(len(g_playerPoints)):

        if g_playerPoints[i] > biggest:
            biggest = g_playerPoints[i]
            index = i

    print(g_player_list[index].upper(), "YOU ARE THE WINNER OF THE GAME")


def roll_again():

    while True:

        response = input("A 1 to Roll or 2 to Quit ")

        if response in ("12"):
            break

    return response

main()


