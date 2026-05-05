#Classes in OOPS

class person:
    name="Akki"
    age=18
    networth =10
    def info(self): #here self is self perameter ,That object that on it method call here a and b  and c is self
        print(f"{self.name} is a {self.age}")

a=person()
b=person()
c=person()
D=person() #Default value collect from function like a 
b.name="nitika"
b.age="17"
c.name="shiv"
c.age=23
a.info()  
b.info()
c.info()  
D.info()    