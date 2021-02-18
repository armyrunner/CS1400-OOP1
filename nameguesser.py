def main():

    #print Insturctions
    print("Welcome to the name guesser. In this challenge you have")
    print("three chances to guess nyname. If you should guess my name,")
    print(" a reward will be in store. However, if you fail to guess my name,")
    print("bad things will happen to you")
    print(" ")
    print(" ")
    #set correct name
    xname = "andrew"
   
    
    #number of guesses
    x = 3

    # give the user 3 tries to guess it
    print("You will have",x,"tries to guess my name")
    print(" ")
    for i in range(x):

        # get the input
        xget = input(" What is your guess -> ")

        if xget == xname:
            print(" You guessed correctly")
            print(" My name is ", xname)
            break
        else:
            print("You have",(x-1)-i,"tries left to guess")
            print(" ")
            
    if xget != xname:
        print("You Lost HAHAHAHA")
        print("Becuase you did not guess my name")
        print("VERY BAD THINGS WILL HAPPEN TO YOU VERY SOON. HAHAHAHA")
    else:
        print(" You win, you are protected from the bad things.")

main()
