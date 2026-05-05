#only one parent class

class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by a animal ")

class dog(animal):#single inheritance 
    def __init__(self,name,bread):
        animal.__init__(self,name,species="dog")
        self.bread= bread 

    def make_sound(self):
        print("Bark!")

d=dog("Dog","Doggerman")
d.make_sound()

a=animal("man","Dog")
a.make_sound()