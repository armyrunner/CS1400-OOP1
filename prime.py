def main():

    print("This program lists the prime numbers to a limit")


    limit = input("What is the upper limit ->")
    limit = int(limit)

    print(listPrime(limit))

def isPrime(num):
    
    for i in range(2,num):
        
        if num% i == 0:
            
            return False
        
    return True

def listPrime(num):

    lst = [] # intialize the list with empty brackets
    
    for i in range(num):
        
        if isPrime(i):
            lst.append(i)
    return lst


main()
