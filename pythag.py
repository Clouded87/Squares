import random
yesorno=0#random.randint(0,1)
finalset=[]
set1="3-4-5"
set2="1-1√3-2"
set3="1-1-1√2"
setlist=[set1, set2, set3]
newitem=0
if yesorno==0:
    set=random.randint(0, 2)
    chosenset=setlist[set]
    chosenset=chosenset.split("-")
    multiple=random.randint(1, 15)
    for i in chosenset:
        newset=i.split("√")
        if len(newset)==2:
            newitem=str(int(newset[0]*multiple))+"√"+newset[1]
        elif len(newset)==1:
            newitem=str(int(newset[0])*multiple)
        finalset.append(newitem)
    print(chosenset)
    print(finalset)