# Local and Global variabal

x = 4 # x is global variable
print(x)


#Global variable
def hello():

    print(x) #Global variable
    print("Hello bro!!!")
hello()

#Local variable
def hello1():
    y=5 #Local variable defined in function 
    print(y)
    print("good morning")

hello1()
# print(y)  Here y is local variable properties of function so y is not print here
print(x)


#GLOBAL KEYWORD

x=10

def function():
    global x # global keyboard that convert here x=10 to x=4 
    x=4  # this will change the value of the global variable x
    y=2 # local veriable
    print(y)

function()
print(x)
# print(y)  Here y is local variable properties of function so y is not print here