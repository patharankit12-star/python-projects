# parents-->child-->child's child

class animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name of animal is : {self.name}")

class Dog(animal):
    def __init__(self,name,bread):
        animal.__init__(self,name)
        self.bread=bread

    def show(self):
        animal.show(self)
        print(f"Bread:{self.bread}")
class seffer(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,bread="Golden Retriever")
        self.color = color 

    def show(self):
        Dog.show(self)
        print(f"color:{self.color}")
    

o = seffer("papyy","black")
o.show()    

o1= Dog("pappy","crawd")
o1.show()

o2 = animal("pappy")
o2.show()