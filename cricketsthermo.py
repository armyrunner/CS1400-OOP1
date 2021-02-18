

#Problem Statement:

# Calculate the temperature by using crickets as the temperature gauage. This is done by counting
# the number of chirps it does in 13 seconds and the you add 40 to that number.  It is approximation to what the
# temperature should be.


# Programmer: Andrew Nelson
# Date: 8-31-2018

def main():


    print("Hey Dipper, I'll calculate the temperature for you.")
    print("Using your stopwatch, count how many times the cricket chirps in 13 seconds.")
    print()
    
    numch = input("How many chirps where there? ")
    numch= float(numch)

    temp = cricketcount(numch)

    if temp > 55:
        return print("By my calculations it is about ", temp, "degrees.")
    else:
        return print("It is too cold for crickets!")


def cricketcount(numch):

    temp = 40 + numch

    return temp

main() 

            
