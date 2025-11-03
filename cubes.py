#I know 0-16, 20, 25
import random
basenum=int(input("Bottom num to study"))
cubes=[]
correct=[]
incorrect=[]
incorrect_internal=[]
for i in range(basenum, 11):
    cubes.append(i)
for i in range(basenum+10, 21):
    cubes.append(i)
random.shuffle(cubes)
def practice():
    global cubes, correct, incorrect, incorrect_internal
    for x in cubes:
        if x>10:
            x=x-10
            responce=int(input("What is the cube root of "+str (x*x*x) +"?"))
            answer=x
            if responce==answer:
                print("Correct")
                correct.append("Cube root of "+str(x*x*x))
            else:
                print("Incorrect it is "+str(answer))
                incorrect_internal.append(x+10)
                incorrect.append("Cube root of "+str(x*x*x))
        else:
            responce=int(input("What is "+str(x)+" cubed?"))
            answer=int(x)*int(x)*int(x)
            if responce==answer:
                print("Correct")
                correct.append(str(x)+" cubed")
            else:
                print("Incorrect it is "+str(answer))
                incorrect.append(str(x)+" cubed")
                incorrect_internal.append(x)
    print(incorrect)
    quit=input("Do you want to continue with incorrect answers?(y/n)")
    if quit=="y":
        cubes=incorrect_internal
        incorrect=[]
        incorrect_internal=[]
        correct=[]
        practice()
    else:
        pass
practice()