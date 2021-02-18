import random


def request_name(player):

    print("Player",player,"Name please", end = " ")
    name = input("-> ")
    greeting(name)

    return name

    return ""


def greeting(name):
    print("Thank you for playing",name)


def roll_dice(sides):

    return random.randrange(1,sides+1)

def roll_again():

    while True:

        response = input("Do you wish 1 -> Roll or 2 -> Quit")

        if response == ("12"):
            break

    return response

def player_turn(name):

    points = 0
    while True:
        roll = roll_dice(6)
        print("You rolled a ", roll)
        print(name, "has", points)

        points += 1

        if roll_again() == "2":
            break
    if points >= 21:
        points = 0

    return points


def play_game(player1,player2):

    while True:

        points1 = player_turn(player1)
        points2 = player_turn(player2)

        if points1 != points2:
            break

    if points1 > points2:
        print(player1, "Wins")
    else:
        print(player2,"Wins")


def main():

    instruction()

    player1 = request_name(1)
    player2 = request_name(2)

    play_game(player1,player2)

def instruction():

    print(" ")

    print(" ")
    print("   Players in turn aim to score 21, or as near as possible to it, by throwing the dice as many times\n"
          " as desired and adding up the numbers thrown. A player who totals over 21 is bust and is out of\n"
          " the game. The player whose total is nearest 21, after each player has had a turn, wins the\n"
          " game. In the case of an equally high total, a play-off is made.\n")
    print(" ")

main()



