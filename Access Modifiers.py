# Access modifiers in public,private and protected modifier
# just normal use not final private and protected
# _ is only normal not provide proceted and __ is private momdifier that provide privacy

#PUBLIC modifiers
class Employee:
    def __init__(self):            
        self.name="isha"

a=Employee()
print(a.name)


#PRIVATE modifiers

class leader:
    def __init__(self):
        self.__name="manali"

b=leader()
 #print(b.__name) cannot access directly in private modifiers
print(b._leader__name) # can be access indirectly

#PROTECTED modifiers

class student:
    def __init__(self):
        self._name="kavita"

    def _fullname(self):   #protected method 
        return "super kavita"
class subject(student):   #inherited method
    def name(self):         
        return "kavya"

obj = student()
obj1 = subject()

# caslling by object of student class
print(obj._name)
print(obj._fullname())

#calling by object of subject class

print(obj1._name)
print(obj1._fullname())
print(obj1.name())

    