"""
This is a Team Manager Software. Allows you to add multiple
Teams and 4 team players to the text file.

Programmer: Andrew Nelson
Intial Code: 11/16/2018


"""


def main():



    instructions()

    filename = input("What is the file name? ->")

    getTeam(filename)


def instructions():

    print("=======================================")
    print("Welcome to Code Camp Team Manager!")
    print("This program will add teams to the Team\n"
          "database file. You can run the program again\n"
          "to add more teams to the file.\n")

    print("Use the other program to display a list of team names.\n")

def getTeam(filename):

    fout = open(filename,"a")

    addteam = "y"

    while addteam == "y":

        team = "Team Name: "
        fout.write(team)

        teamname = input("What is your team name? ->")
        fout.write(teamname+"\n")
        print(" ")
        count = 0
        addplayer = "y"

        while count < 4 and addplayer == "y":
            member = "Member Name: "
            fout.write(member)

            memembername = input("What is a teammate name?")
            fout.write(memembername+"\n")
            print(" ")
            if count < 3:
                addplayer = input("Is there another team member?")
                if addplayer != "y":
                    fout.write("\n")

            count += 1

        addteam = input("Is there another team?")

    fout.close()


    return teamname, memembername

main()