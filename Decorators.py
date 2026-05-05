
# Decorator function for wishes and add start and botttom

#Create Decorator function 
def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("Thank for using this function")
    return mfx

@greet #modify function 
def hello():
    print("hello world")
@greet
def fun():
    print("nice to meet you")
@greet
def fun1(a,b):   #normally call greet 
    print(a+b)
hello()
fun()
fun1(1,3)

greet(hello())
greet(fun())
greet(fun1)(1,3)

    