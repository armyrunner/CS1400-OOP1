# Highway Travelor Advisor
# Andrew Nelson
# Intial Code -- 09/18/2018
# Revised -- 09/21/2018


def main():

    
    # Instructions for the Highway Travelor Advisor
    
    print("Welcome to the Highway Travelor Advisor.")
    print("This application has been configured to work with")
    print("travel on I-15 with the state of Utah. We'll ask for")
    print("a few pieces of information, then give you advice on your travel")
    print(" ")
    #User Input

    start = input("Enter I-15 at what mile marker? ->")
    finish = input("Exit I-15 at what mile marker? ->")
    hours = input("How many hours from now do you want to arrive? ->")
    mph = input("Expect average speed in MPH? ->")
    print("")

    #convert from string to float
    start = float(start)
    finish = float(finish)
    hours = float(hours)
    mph = float(mph)
    
    #print out the resutls
    print("You will travel:",distance(start,finish),"miles")

    # new variables
    newHours = timeTravel(start,finish, hours, mph)
    time = newTime(start, finish, hours,mph)

    # traveling to fast or slow or normal

    if mph > 80:
        print("Your speed is dangerously high. Slow Down!!!")
        print("Thanks for using the highway travel advisor.")
    elif mph <= 80 and mph >= 60:
        if newHours < hours:
            print("Leave in the next",time,"hours to be on time.")
            print("Thanks for using the highway travel advisor.")
        else:
            print("You won't be able to get there on time. You will be", time, "hours late.")
            print("Thanks for using the highway travel advisor.")
    else:
        print("Your traveling to slow. You will hinder the traffic")
        print("Thanks for using the highway travel advisor.")
            
def distance(start,finish):

    total = 0
    total = finish - start

    return abs(total)

# average speed for travleing
def timeTravel(start,finish, hours, mph):

    newHours = 0
    newHours = distance(start,finish)/mph
    
    return newHours

def newTime(start, finish, hours,mph):

    time = 0

    if  hours > timeTravel(start,finish, hours, mph):
        time = hours - timeTravel(start, finish, hours, mph)
    else:
        time = timeTravel(start,finish,hours,mph) - hours
        
    return time

main()
