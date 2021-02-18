import random

def main():
    filename = "roll.txt"

    print(" Welcome to the Class Participation \n"
          "Manager System.")
    print(" ")
    print(" I will randomly pick students for you.")

    print(" What is the name of your file",filename)
    print(" ")

    pickname(filename)

def pickname(filename):

    fin = open(filename,'r')

    lst = []

    while True:

        for line in fin:

            lst.append(line.strip())

        randindex = random.randrange(0,len(lst))

        name = lst[randindex]
        print(name)
        x = input("Enter q to quit. ->")

        if x == "q":
            break

    fin.close()


main()