# custom error ...

a=input("enter any value between 5 and 9:")

# raising custom errror

if(a=="quit"):
     print(a)

elif(int(a)<5 or int(a)>9):
     raise ValueError("value should be between 5 and 9")
# when value not between 5 to 9 that is executed 





