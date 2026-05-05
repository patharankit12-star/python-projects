
#Hybrid Inheritance
# combine of single and multiple inheritance that over all call Hybrid Inhritance

class Baseclass:
    pass
class Derived1(Baseclass):
    pass
class Derived2(Baseclass):
    pass
class Devired3(Derived1, Derived2):
    pass

#Hieraerchical Inheritance

class Baseclass:
    pass
class D1(Baseclass):
    pass
class D2(Baseclass):
    pass
class D3(D1):
    pass
class D4(D1):
    pass
class D5(D2):
    pass