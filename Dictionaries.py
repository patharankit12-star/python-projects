# Dictionaries in python 

age=input("enter your age:")
gender=input("enter your gender:")

dic={ age:"child",
     gender:"male"}

print(dic[age])

# Example

dic={
    344:"Harry",
    56:"shubham",
    28:"Neha",
    10:"meet",
    12:"smet"
    }
n=int(input("Enter id:"))
print(dic[n])

#Example form info

info={'name':'karan','age':19,'eligible':True}
print(info)
print(info['name'])
print(info.get('age2')) #not give error if key nopot exist
print(info.keys()) # All keys 
print(info.values())

# keys 
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


print(info.items())
# items
for key , value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
