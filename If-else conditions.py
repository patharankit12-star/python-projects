#string in if-else
a=int(input("enter your age: "))
print("your age is: ",a)
#Conditional Operatoes
# > , < , >= , <= , == , !=
print(a<18)
print(a>18)
print(a>=18)
print(a<=18)
print(a!=18)
if(a>18):
    print("You can drive ")
    print("yes")
else:
    print("You can not drive car")
    print("No") #space is matter
print("Thank you")   

#if-elif-else condition

N=int(input("enter the number:"))
print("your numbar is:",N)
if(N<0):
    print("numberm is nagative!")
elif(N==0):
    print("nuber is Zero!")
elif(N!=0):
    print("number is non-Zero!")
else:
    print("number is positive!")

print("Again Thank you!")

#Nested if statements

num=18
if(num<0):
  print("number is negative")
elif(num>0):
    if(num <= 10):
     print("number is between 1-10")
    elif(num >10 and num <=20):
     print("number is between 11-20")
    else:
     print("number is greater than 20")
else:
   print("number is zero")

   # TASK: with if-elif-else

import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

if(int(time.strftime("%H")) >=6 and int(time.strftime("%H")) <12):
   print("good morning")
elif(int(time.strftime("%H")) >=12 and int(time.strftime("%H")) < 20):
   print("good evening")
elif(int(time.strftime("%H")) >=20):
    print("good night")
else:
   print("Enter correct time")