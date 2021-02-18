# Andrew Nelson
# Write a program to do the following
# User input for dimensions of the tank
# User input for the amount of rain water
# Convert inches to feet
# Global Variable for gallons per cubic foot

# Started:9-8-2018
# Revisison 1:

# gcpf stands Gallons per Cubic Foot
gpcf = 7.48
gpcf = float(gpcf)
inchFeet = 12
inchFeet = float(inchFeet)

def main():

    print("Welcome to the rainwater tank calculator.")
    print("We'll ask you for a few parameters about your rainfall ")
    print("and rain catchment area. We assume that your catchment ")
    print("area is rectangular.")
    
    print()
    
    rainFall =  float(input("How many inches of rain fall in a large storm? -> "))
    wideth = float(input("How wide is your catchment area, in feet? -> "))
    long =  float(input("How long is your catchment area, in feet? -> "))
    
    print()
    print("You need a tank with ",gallons(wideth,long,rainFall),"gallon capacity")
    print("to capture that much rain at one time")


def conInchFeet(rainFall,inchFeet):
    conTotal = 0
    conTotal = float(conTotal)
    conTotal = rainFall / inchFeet

    return conTotal
    

def volume(wideth,long,rainFall):
    boxTotal = 0
    boxTotal = float(boxTotal)
    boxTotal = wideth * long * conInchFeet(rainFall,inchFeet)
    
    return boxTotal

def gallons(wideth,long,rainFall):
    galTotal = 0
    galTotal = float(galTotal)
    galTotal = volume(wideth,long,rainFall) * gpcf

    return galTotal

main()
