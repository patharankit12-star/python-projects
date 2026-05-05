# Error Handling in finally always exicuted



def func1():
   try:
      l=[1,2,3,4]
      i=int(input("Enter the index:"))
      print(l[i])
      return 1
   except:
      print("some error occurred")
      return 0
   finally:
      print("I am always executed") # in function return yet also finally executed that main purpose of finally

x=func1()
print(x)   
            