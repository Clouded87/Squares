import random
yesorno=0#random.randint(0,1)
finalset=[]
set1="3-4-5"
set2="1-1√3-2"
set3="1-1-1√2"
setlist=[set1, set2, set3]
if yesorno==0:
    set=random.randint(0, 2)
    chosenset=setlist[set]
    chosenset=chosenset.split("-")
    multiple=random.randint(1, 15)
    for i in range(chosenset):
        newitem=str(int(chosenset[i])*multiple)
        finalset.append(newitem)
    print(chosenset)