"""
Program is to change from leet speak to English to be able to understand
what is being said in the text.

Programmer: Andrew Nelson
Intial Program: 11/3/18

Revision 1: 11/5/2018 - able to translate from leet speak to english
Revision 2: 11/7/2018 - able to translate from english to leet speak
Revision 3: 11/8/2018  - able to choose which one to translate

"""



def main():

    leet_letters = "48CD3FGHIJK1MN0PQR57UVWXYZ@bcd3fghijk1mn0pqr57uvwxyz "
    eng_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

    printInstructions()

    userinput = input("Choose the Following\n"
                      "1) Translate from Leet Speak to English\n"
                      "2) Translate from English to Leet Speak\n"
                      "Your Choose is: ")
    userinput = int(userinput)

    if userinput == 1:

        filename1 = input(" Leet file name? ->")
        filename2 = input(" English file name? ->")

        getfile(filename1, filename2, leet_letters, eng_letters)

    elif userinput == 2:

        filename3 = input( " Enter English File name")
        filename4 = input(" New leet file name? -> ")

        getfile2(filename3,filename4,leet_letters,eng_letters)



def printInstructions():
    print(" ")
    print("=====================================================================")
    print(" Welcome to the Leet Speak Translator! ")
    print(" ")
    print(" If you have a file that is written in leet speak, we can \n "
          "translate it back to normal English for you. ")
    print(" ")
    print("Just give me the name of the file your want to have translated, \n"
          "and the name you want for the translated file. ")
    print("=====================================================================")
    print(" ")

def getfile(filename1,filename2,leet_letters,eng_letters):

    fin = open(filename1,'r')
    fout = open(filename2, 'w')

    for line in fin:
        line = line.strip()

        for char in line:
            pos = leet_letters.find(char)

            if pos == -1:
                fout.write(char.upper())
            else:
                fout.write(eng_letters[pos].upper())

        fout.write("\n")

    fout.close()
    fin.close()

def getfile2(filename3,filename4,leet_letters,eng_letters):

    fin = open(filename3, 'r')
    fout = open(filename4, 'w')

    for line in fin:
        line = line.strip()
        for char in line:
            pos = eng_letters.find(char)

            if pos == -1:
                fout.write(char.lower())
            else:
                fout.write(leet_letters[pos].lower())

        fout.write("\n")

    fout.close()
    fin.close()


main()