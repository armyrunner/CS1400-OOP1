# fahrenheit to celsuis
#bob Nielson
# sep 4, 2018

def main():

    f = input("Enter the temperature in Fahrenheit ? ")
    f = float(f)
    c = ftoc(f)

    print(" Your temperature in Celsius is"+str(c))
    

# f = fahrenheit temp
# c = celsius temp

def ftoc (f):
    c = (f-32)*5/9
    return c

main()
