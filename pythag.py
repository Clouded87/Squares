import random
yesorno=random.randint(0,1)
finalset=[]
set1=["3", "4", "5"]
set2=["1", "1√3", "2"]
set3=["1", "1", "1√2"]
set4=["5", "12", "13"]
set5=["8", "15", "17"]
set6=["7", "24", "25"]
set7=["1", "2", "1√5"]
setlist=[set1, set2, set3]
newitem=0
fakelist=[]
multiple=random.randint(1, 15)
if yesorno==0:
    set=random.randint(0, 6)
    chosenset=setlist[set]
    for i in chosenset:
        newset=i.split("√")
        if len(newset)==2:
            newitem=str(int(newset[0])*multiple)+"√"+newset[1]
        elif len(newset)==1:
            newitem=str(int(newset[0])*multiple)
        finalset.append(newitem)
    print(finalset)
if yesorno==1:
    for x in range(0, 3):
        fakeitem=random.randint(1, 17)*multiple
        fakelist.append(fakeitem)
    print(fakelist)
x=input("Is this a triple?(y/n)")
if yesorno==0:
    if x=="y":
        print("Correct")
    if x=="n":
        print("Incorrect")
    for i in range(0, 3):
        x=input("What is the "+str(i+1)+" digit")
        if x==chosenset[i]:
            print("Correct")
        elif x!=chosenset[i]:
            print("Incorrect")
elif yesorno==1:
    if x=="y":
        print("Incorrect")
    if x=="n":
        print("Correct")
