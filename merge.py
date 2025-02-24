import random
basenum=int(input("Bottom num to study"))
squares=[]
correct=[]
incorrect=[]
incorrect_internal=[]
for i in range(basenum, 26):
    squares.append(i)
for i in range(basenum+25, 51):
    squares.append(i)
random.shuffle(squares)
def practice():
    global squares, correct, incorrect, incorrect_internal
    for x in squares:
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
    print(incorrect)
    quit=input("Do you want to continue with incorrect answers?(y/n)")
    if quit=="y":
        squares=incorrect_internal
        incorrect=[]
        incorrect_internal=[]
        correct=[]
        practice()
    else:
        pass
practice()