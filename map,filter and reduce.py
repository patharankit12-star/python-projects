
#MAP
def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,5]
newl=[]

for i in l:
    newl.append(cube(i))
    
print(newl)

#use map function 

#newl=list(map(cube,l))
newl=list(map(lambda x:x*x*x,l)) # use lambda function
print(newl)

#FILTER

def filter_function(a):
    return a>2

#newnewl=list(filter(filter_function,l))

newnewl=list(filter(lambda x : x>2 , l)) #use lambda function 
print(newnewl)

# REDUCE 
# import resude function 

from functools import reduce 

#list of num\

num=[1,2,3,4]

#calculate the sum of num using resude function 
def mysum(x,y):
    return x + y #as per your thought +,-,*,/

sum = reduce(mysum,num)
print(sum)
