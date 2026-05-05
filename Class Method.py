# class method 

#change in class 

class Employee:
    company="Apple"
    def show(self):
        print(f"Employee name is {self.name} and company name is {self.company}")
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany


e1=Employee()
e1.name="Harry"
e1.show()
e1.changecompany("Tesla")

e1.show()   #Tesla
print(Employee.company) #Apple but we use @classmethod that convert into new update 