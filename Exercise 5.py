#                 S W G
# computer =      0 1 2 
# player  = S 0   D W L   
#           W 1   L D W
#           G 2   W L D
#

'''c=input("com:enter 0 for snack,enter 1 for water ,enter 2 for gun:")
p=input("user:enter 0 for snack,enter 1 for water ,enter 2 for gun:")

snake=0
water=1
gun=2

if c is p:
    print("D")
elif p>c:
    if c==0:
        print("w")
    else:
        print("L")
        
else:
    if p==0:
        print("L")
    else:
        print("w") '''


import random

def check(comp,user):
    if comp==user:
        return 0

    if(comp==0 and user==1):
        return -1 
    if(comp==1 and user==2):
        return -1 
    if(comp==2 and user==0):
        return -1
    
    return 1

comp=random.randint(0,2)
user=int(input("0 for snake ,1 for water and 2 for gun:\n"))

score = check(comp,user)

print("you:",user)
print("computer:",comp)

if(score == 0):
    print("it's draw")
elif (score == -1):
    print("you lose")
else:
    print("you won")









'''if com==player:
    print("D")

elif com==snake and player==water:
    print("L")
elif com== gun     and player==snake    :
    print("L")
elif com==  water  and player== gun:
    print("L")
    
elif com==water and player==snake:
    print("w")
elif com==gun      and player==water   :
    print("w")
elif com==snake   and player==gun  :
    print("w")
else:
    print("play again!!!")'''
    
