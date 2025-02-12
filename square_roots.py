import random
basenum=int(input("Bottom num to study"))
squares=[]
for i in range (basenum, 26) :
    squares.append(i)
random.shuffle(squares)
for x in squares:
    responce=int(input("What is the square root"+str (x*x) +"?"))
    answer=x
if responce==answer:
    print("Correct")
else:
    print("Incorrect")
