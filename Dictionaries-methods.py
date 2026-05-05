#Dictionaries methods

#Update() enter 2 in 1

ep1={122:67,
     123:68,
     124:69,
     125:70,
     126:71
     }
ep2={127:72,128:73}
print(ep1)
print(ep2)
ep1.update(ep2) # Add ep2's value in ep1
print(ep1)
ep2.clear() #clear whole Dictionarie
print(ep2)
ep1.pop(122) # remove 122 key and its value
print(ep1)
ep1.popitem() # Remove last key and its value
print(ep1)
# del ep1 delete whole dictionaries

del ep1[124] # delete specific key 
print(ep1)