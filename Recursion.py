# call function in function that is Recursion 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) # That is recursion 
    
print(factorial(6))

#fibonaci seris 

def fibonaci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
       

n=int(input("enter your numbers:"))    

for i in range(n):
    print(fibonaci(i),end=" ")



    
    