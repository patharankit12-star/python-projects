
class math:

 def __init__(self , num):
    self.num=num

 def addtonum(self,n):
   self.num = self.num + n

# not always require that class in self parameter in class into funtion ,static method not use self parameter indivisual use this method
 @staticmethod
 def add(a,b):
    return a + b
    

a=math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(math.add(9,8)) #also call as class
print(a.add(7,3))