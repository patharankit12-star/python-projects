# foe constructors for __init__ required

class person:

    def __init__(self,name,occ):  #Constructors function use __init__ is special keybord for this function .that repalce name="Akki" age=18
    
        print("Hey I am a person")
        self.name=name
        self.occ=occ
    def info(self):
        print(f"{self.name} is a {self.occ}.")

    
    
a=person("Akki","developer")
b=person("nitika","Hacker")

a.info() #print(a.name)
b.info() 
    