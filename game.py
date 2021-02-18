import random
import time

def getHigh():

    fin =open("highscore.txt","r")
    for line in fin:
        lst = line.strip()
        lst = line.split()

    fin.close()
    return lst[0],int(lst[1])

def getScore():

    fin =open("gamescore.txt","r")
    for line in fin:
        lst = line.strip()
        lst = line.split()

    fin.close()
    return lst[0],int(lst[1])


def putHigh(name,score):
    fout = open("highscore.txt",'a')
    fout.write(name+" "+str(score)+"\n")
    fout.close()


def putScore(name,score):
    fout = open("gamescore.txt",'a')
    fout.write(name+" "+str(score)+"\n")
    fout.close()

def rollDice(sides):
    return random.randrange(1,sides+1)


def playGame():
    tot = 0
    for i in range(16):
        num = rollDice(6)
        tot += num
        print(num,end=" ")
        time.sleep(1)
    print()
    return tot


def main():

   name,highscore=getHigh()

   print("WELCOME TO BOBS GAME")
   print("The current high score is", highscore)
   print("The here of the this game is ", name)
   print("  ")

   print("====================================")

   print("  ")
   name, highscore = getScore()

   print("The current score is", highscore)
   print("The here of the this game is ", name)

   score = playGame()

   print("Your Score is -->",score)

   if score > highscore:
       print("Congrats you got the High Score")
       name = input(" What is your name? ->")
       putHigh(name,score)
   elif score < highscore:
       print("Your Score is ->")
       name = input(" What is your name? ->")
       putScore(name, score)



main()