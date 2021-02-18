# quadratic equation solver
# Andrew Nelson

# Intial - 09/18/2018

def main():

    # print instructions

    print(" This program solves the quadratic equation.")
    print("")
    print("   ax^2+bx+c=0")
    print("")

    # get user input

    a = input(" What is a ->")
    b = input(" What is b ->")
    c = input(" What is c ->")

    # convert a,b,c, to float

    a = float(a)
    b = float(b)
    c = float(c)

    #call the quadrtic function

    r1 = quadplus(a,b,c)
    r2 = quadneg(a,b,c)

    #print results
    print("Root 1 ->", r1)
    print("Root 2 - >", r2)

    # verify resutls
    print("Verify #1 ->", a*r1*r1+b*r1+c)
    print("Verfiy #2 ->", a*r2*r2+b*r2+c)

    

def quadplus(a,b,c):
    det = (b*b-4*a*c)**.5
    root1 = (-b+det)/(2*a)
    
    return root1

def quadneg(a,b,c):
    det = (b*b-4*a*c)**.5
    root2 = (-b-det)/(2*a)
    
    return root2
    

main()
