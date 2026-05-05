# Error Handling .....
#use full in  procect from creash programme
a=input("Enter the number: ")
print(f"Multiplication table of {a} is:")
""" try:
        code......
    except Exception as e:
        print(e) #print error """
try:                                                
      for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("some important in code")
print("End of program")
""" try:
       code......
    except ValueError:
        code...
    except IndexError:
        code....."""
try:
    num= int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer,")
except IndexError:
    print("Index Error")
     
