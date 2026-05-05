#dir() return list of all the attributes and methods(including dunder methods) in list ,tuple etc..

x = [1,2,3]
print(dir(x)) #give all method that can we use in list ,tupple and etc..
'''['__add__', '__class__', '__class_getitem__', 
'__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
 '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
   '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
   '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
     '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
     'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']'''
print(x.reverse)

#__dict__ - That use to find all attribute from class componects 

class person:
    def __init__(self , name , age):
        self.name=name
        self.age=age
        self.version=1

p=person("john",20)
print(p.__dict__) #{'name': 'john', 'age': 20,'version':,1}

# help method 
#give all details that in class
print(help(person))


