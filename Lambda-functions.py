
# Lamda-function use that short from of function 

#def double(x):
#   return x*2

# use lambda function 
double=lambda x: x*2

#def cube(x):
 #  return x*x*x
cube=lambda x:x*x*x

print(double(5))
print(cube(3))

#def avg(x,y):
#    return (x + y)/2

avg=lambda x,y : (x + y)/2

print(avg(3,5))

#function pass as arguments

'''def appl(fx,value):
    return 6 + fx(value)

print(appl(avg,2,4)) '''