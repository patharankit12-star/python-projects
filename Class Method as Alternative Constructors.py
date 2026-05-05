# class method use in constructor

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"name of Employee is {self.name} and salary is {self.salary}")
    @classmethod
    def fromstr(cls ,string): # CLASS METHOD as olternative constructors
        return cls(string.split("-")[0] , string.split("-")[1])
    
e1= Employee("Rahul",22000)

string = "john-12000"
e2 = Employee.fromstr(string) #class method 

