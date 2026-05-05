# magic methods in class

#__len__ method 
class Employee:
    name="Harry"
    id="Harry1"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    #__str__method
    def __str__(self):
        return f"The name of the employee is {self.name} str "
    
    #__repr__method
    def __repr__(self):
        return f"Employee'{self.name}'"

    #__call__method

    def __call__(self):
        print("Hey , I am good.")



    
e=Employee()
print(e.name)
print(len(e)) 

#__str__ method
print(str(e))

#__repr__method
print(repr(e))

#__call__ method
e()

