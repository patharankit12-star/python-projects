class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"The name of enployee:{self.id} is {self.name}")
class programmer(Employee):
    def show1(self):
        print("The default langauge is python")

#create object outside the class    
E1=Employee("amit",420)
E2=programmer("nikita",440)

E1.show()
#E2.show()


#use INHERITANCE
E2.show() 
E2.show1()
