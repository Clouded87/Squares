import random
basenum=int(input("Bottom num to study"))
squares=[]
for i in range(basenum, 26):
    squares.append(i)
for i in range(basenum-25, 51):
    squares.append(i)
random.shuffle(squares)
for x in squares:
    if x<25:
        responce=int(input("What is the square root of "+str (x*x) +"?"))
        answer=x
        if responce==answer:
            print("Correct")
        else:
            print("Incorrect it is "+str(answer))
    else:
        responce=int(input("What is "+str(x)+" squared?"))
        answer=int(x)*int(x)
        if responce==answer:
            print("Correct")
        else:
            print("Incorrect")  
