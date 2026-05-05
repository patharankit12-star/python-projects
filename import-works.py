

#join with try..py
#from Try import welcome,name           #take from other files 
from Try import *


import math

result=math.sqrt(9)
print(result) # Outrput=3.0

#from keyword

from math import sqrt 

result=sqrt(9)
print(result) #output=3.0

from math import sqrt,pi

result=sqrt(9) * pi  #OTHERWISE Try from math import *
print(result)
print(pi)

#"as" keyword

from math import pi,sqrt as s #sqrt convert into as 

result=s(9)*pi
print(result) 


import math as m #math convert into m

result=m.sqrt(9)*pi
print(result)

#print all function in import 

import math
print(dir(math))
#example
print(math.nan , type(math.nan))

print(name)
welcome()
print(name)