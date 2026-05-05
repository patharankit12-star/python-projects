# is vs ===

a=[1,2,3] # is vs == different in set 
b=[1,2,3]

print(a is b) #exact location of object in memory
print(a==b)  # value

a="harry"
b="harry"

print(a is b)
print(a==b)

a=3
b=3

print(a is b)
print(a==b)

# none

a=None
b=None

print( a is b)
print(a==b)
print( a is None )