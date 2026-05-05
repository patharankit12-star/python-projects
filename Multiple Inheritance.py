#one or more parents class

class Employee:#parentsclass
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Name of the Employee is {self.name} ")
class Dancer:#parentsclass
    def __init__(self,Dance):
        self.Dance=Dance
    def show(self):
        print(f"Dance of the Employee is {self.Dance} ")
class DancerEmployee(Employee,Dancer):#childclass

    def __init__(self,name,Dance):
        self.Dance=Dance
        self.name=name

o= DancerEmployee("shivani","kathak")
print(o.name)
print(o.Dance)
o.show() #childclass in name is first so first of all employee() is print 

