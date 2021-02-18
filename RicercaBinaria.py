import random

def main():

    print(" I will pic a number between 1 and a 100, inclusive."
          "Try to quess my number in as few guesses as possible."
          "Don't worry, I'm a nice program. I'll give you hints."
          "Good Luck!!!")

    print(" ")
    print(" ")
    print(" ")
    print("Okay I have my number! Start Guessing!")
    print(" ")
    print(" ")
    print("It took you", picknum(),"tries")

def picrandnum():

    picnum = random.randrange(1,101)

    return picnum


def picknum():

    count = 0

    num = picrandnum()

    while num != True:

        guess = int(input("What is your guess? ->"))

        if guess > num:
            print(" Too High")
            count +=1

        elif guess < num:
            print("Too Low")
            count +=1
        else:
            print(" ")
            print("Your Guessed the right number!!!")
            print("Congraduations!! Your Won!!!")
            break

    return count


main()
