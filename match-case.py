#Similar to switch case in C langauge

x=int(input("Enter value of x (0-4):"))

# x is variable to match

match x:
    case 0:
        print("x is Zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3:
        print("x is three")
    case 4:
        print("x is four")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x,"is not 80")
        