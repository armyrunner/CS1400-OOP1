"""
Program: Multiplication Quiz
Programmer: Andrew Nelson
Intial Code: 10-24-2018
revised: 10-26-2018


"""

import random
import time

def main():

    print(" ")
    print (" WELCOME TO THE MULTIPLECATION QUIZ!")
    print("  ")

    name = input("What is your Name?")

    print("  ")
    print("Welcome",name," to  the Multipication Quiz. My name is Mr. Multiply."
            " Try to multiply your time table facts quickly as possible! ")
    print("  ")
    print("I'll will ask you the multiplication questions, and you just answer them as quick  "
          "as possible. For every wrong answer a 5 second penalty will be add at the end.")
    print(" ")

    multilevel = ("Choose a Difficulty level:\n 1)For Beginner\n 2)Intermediate\n 3)Advanced\nEnter Value -> ")
    multiTable = ("Choose a Value 1-12 you want to multiply and hit Enter to Start the quiz->")

    multiplicationQuiz(multiTable,name,multilevel)

def multiplicationQuiz(multiTable,name,multilevel):

    lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    level = int(input(multilevel))

    total = 0
    count1 = 0
    count2 = 0

    if level == 1:

        value = int(input(multiTable))

        start = time.time()

        for i in range(len(lst1)):

            ca = value*lst1[i]
            print("  ")
            guess = int(input(str(value) + " x " + str(lst1[i]) + " " + "= "))
            count1 += 1

            while ca != guess:
                print(" ")
                print(" OOPS! Wrong Answer. Try Again! 5 second penalty applied")
                print("  ")
                guess = int(input(str(value) + " x " + str(lst1[i]) + " " + "= "))
                count2 += 1

    elif level == 2:

        value = int(input(multiTable))

        start = time.time()
        var1 = lst1
        random.shuffle(var1)

        for i in range(len(var1)):

            ca = value * var1[i]
            print("  ")
            guess = int(input(str(value) + " x " + str(var1[i]) + " " + "= "))
            count1 += 1

            while ca != guess:
                print(" ")
                print(" OOPS! Wrong Answer. Try Again! 5 second penalty applied")
                print("  ")
                guess = int(input(str(value) + "x" + str(var1[i]) + " " + "= "))
                count2 += 1

    elif level == 3:

        start = time.time()

        var2 = lst1
        random.shuffle(lst1)


        for i in range(len(var2)):

            var1 = random.randrange(0,13)

            ca = var1 * var2[i]
            print("  ")
            guess = int(input(str(var1) + " x " + str(var2[i]) + " " + "= "))
            count1 += 1

            while ca != guess:
                print(" ")
                print(" OOPS! Wrong Answer. Try Again! 5 second penalty applied")
                print("  ")
                guess = int(input(str(var1) + " x " + str(var2[i]) + " " + "= "))
                count2 += 1

    end = time.time()
    total = (end - start) +(count2*5)

    if total <= 25.0:
        print(" Excellent Job!",name," Your Got",count1,"correct.")
        print(" You Got", count2,"all wrong answers gets a  5 sec. penalty.")
        print(" Your time is ", total)

    elif total > 25.0 and total <= 40.0:
        print(" Great Job!", name, " Your Got", count1, "correct")
        print(" You Got", count2, "all wrong answers gets a  5 sec. penalty.")
        print(" Your time is ", total)
        print(" Keep Going you can go faster than that!!")

    elif total > 40.0 and total <= 60.0:
        print(" Good Job!", name, " Your Got", count1, "correct")
        print(" You Got", count2, "all wrong answers gets a  5 sec. penalty.")
        print(" Your time is ", total)
        print(" A little more practice and you can be Great!")

    else:
        print(name, " Your Got", count1, "correct")
        print(" You Got", count2, " all wrong answers gets a  5 sec. penalty.")
        print(" Your time is ", total)
        print("Keep practicing. The more you practice the better you will get!!")

main()