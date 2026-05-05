# break statement

for i in range(10):
    if(i==9):
      break # exit whole loop
    print(" 5 x",i+1,"=",5*(i+1))

# continue statement 
for j in range(12):
    if(j == 10):#skip num10 iteration
      print("Skip the iteration")
      continue
   
    print("5 x", j,"=",5 * j)

#Task with loop like Do-while loop

i=0
while True:
   print(i)
   i = i + 1
   if(i%100 == 0):
      break 