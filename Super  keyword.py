# call old parents class from child class that use super() keyword 

class parentclass:
    def parent_method(self):
        print("This is parent's class.1")

class childclass(parentclass):
    def parent_method(self):
        print("Rahul")
    def child_method(self):
        print("This is child's class.2")
        super().parent_method()


result= childclass()
result.parent_method()
result.child_method()


# Example 

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id) #super words
        self.lang=lang

rohan= Employee("Rohan","420")
harry=Programmer("Harry","890","python")
print(rohan.name)
print(rohan.id)
print(harry.name)
print(harry.id)
print(harry.lang)

