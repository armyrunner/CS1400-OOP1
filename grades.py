

#  grades - Andrew Nelson


MAXSTUDENTS = 3

def main():
    scores = []
    initScores(scores)
    getScores(scores)
    printScores(scores)
    print()
    print("Ave =  " ,str(calcAve(scores)))

    
def initScores(scores):

    for i in range(MAXSTUDENTS):
         scores.append(0)

def getScores(scores):
    for i in range(len(scores)):
        print("Sudent ", str(i + 1))
        score = input("   Score => ")
        score = int(score)
        scores[i] = score

def printScores(scores):
    for i in range(len(scores)):
        print( "Stundent " ,  i, "Got a" , scores[i])

def calcAve(scores):
    kount = 0
    scoreTot = 0
    for i in range(MAXSTUDENTS):
        kount = kount +1
        scoreTot = scoreTot + scores[i]
    return scoreTot/kount
main()
