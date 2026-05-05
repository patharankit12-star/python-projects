#instance and class variables

#instance: personal variable 
#class : class variable is global variable if instance not defind that class variable is universal uses



class Employee:
    companyname="Apple" # class variables or global variables
    noofEmployer=0
    def __init__(self , name):
        self.name=name
        self.raise_amount=0.02
        Employee.noofEmployer +=1

    def ShowDetails(self):
        print(f"The name of the Employer is {self.name} and the raise amount in {self.noofEmployer} sized {self.companyname} is {self.raise_amount} ")



#Employee.ShowDetails(emp1)
emp1=Employee("Amit")
emp1.raise_amount=0.3
emp1.companyname="Apple india"
emp1.ShowDetails()

emp2=Employee("Nikita")
emp2.raise_amount=0.5 #intance variables
# company name take from class variables
emp2.ShowDetails()
    