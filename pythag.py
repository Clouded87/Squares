import random
triple1=""
triple2=""
triple3=""
triple4=""
triple5=""
triple6=""
triple7=""
triples=[triple1, triple2, triple3, triple4, triple5, triple6, triple7]
#yn=random.randint(0,1)
yn=0
if yn==0:
    triple=str(str(random.randint(0, 20))+", "+str(random.randint(0, 20))+", "+str(random.randint(0, 20)))
#else:
#    random.shuffle(triples)
#    triple=triples[0]
split=triple.split(" ,")
mult_val=random.randint(1, 10)
print_list=[]
for i in split:
    print(i)
    i=triples[i]*mult_val
    print_list.append(str(i))
print_value=", ".join(print_list)
print(print_value)
