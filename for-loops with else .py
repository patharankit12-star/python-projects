# for loops in else if for loop not run that else exicute 

for i in range(5):
    print(i)

else:
    print("sorry for loop not exicute")


# infinate loop

for i in []:
    print(i)
else:
    print("sorry for loop not exicute")

# example

for i in range(6):
    print(i)
    if(i==4):
        break
# loop sucessfully end that else not exicute if break that sucessfully end 
else:
    print("stop")


# while loop
i=0
while i<7:
    print(i)
    i= i + 1
else:
    print("stop")
