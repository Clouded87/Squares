#I know 0-16, 20, 25
import random
basenum = int(input("Bottom num to study"))
basenumcube = int(input("Bottom num to study for cubes"))
squarescube = []
correctcube = []
incorrectcube = []
incorrectcube_internal = []
correct = []
incorrect = []
incorrect_internal = []

cubes = []
for i in range(basenumcube, 11):
    cubes.append(i)
for i in range(basenumcube+10, 21):
    cubes.append(i)
random.shuffle(cubes)
squarescube.append(cubes)

squares = []
for i in range(basenum, 26):
    squares.append(i)
for i in range(basenum+25, 51):
    squares.append(i)
random.shuffle(squares)
squarescube.append(squares)

def practice():
    global squares, cubes, squarescube, correctcube, incorrectcube, incorrectcube_internal, basenum, basenumcube, correct, incorrect, incorrect_internal
    randomchoice = 0
    for x in len(squarescube[0])+len(squarescube[1]):
        if len(squarescube) == 2:
            randomchoice = random.randint(0, 1)
        else:
            pass
        if randomchoice == 0:
            x=squarescube[0][0]
            squarescube[0].remove(x)
            if x>10:
                x=x-10
                responce=int(input("What is the cube root of "+str (x*x*x) +"?"))
                answer=x
                if responce==answer:
                    print("correctcube")
                    correctcube.append("Cube root of "+str(x*x*x))
                else:
                    print("Incorrectcube it is "+str(answer))
                    incorrectcube_internal.append(x+10)
                    incorrectcube.append("Cube root of "+str(x*x*x))
            else:
                responce=int(input("What is "+str(x)+" cubed?"))
                answer=int(x)*int(x)*int(x)
                if responce==answer:
                    print("correctcube")
                    correctcube.append(str(x)+" cubed")
                else:
                    print("Incorrectcube it is "+str(answer))
                    incorrectcube.append(str(x)+" cubed")
                    incorrectcube_internal.append(x)
            if len(squarescube[0]) == 0:
                squarescube.pop(0)
                randomchoice = 1
        if randomchoice == 1:
            x=squarescube[1][0]
            squarescube[1].remove(x)
            if x>25:
                x=x-25
                responce=int(input("What is the square root of "+str (x*x) +"?"))
                answer=x
                if responce==answer:
                    print("Correct")
                    correct.append("Square root of "+str(x*x))
                else:
                    print("Incorrect it is "+str(answer))
                    incorrect_internal.append(x+25)
                    incorrect.append("Square root of "+str(x*x))
            else:
                responce=int(input("What is "+str(x)+" squared?"))
                answer=int(x)*int(x)
                if responce==answer:
                    print("Correct")
                    correct.append(str(x)+" squared")
                else:
                    print("Incorrect it is "+str(answer))
                    incorrect.append(str(x)+" squared")
                    incorrect_internal.append(x)

practice()