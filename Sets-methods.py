#Sets methods

s1={1,2,3,4,5,3}
s2={3,4,5,3,6,7,8}

#s1.union(s2) merge both set 

print(s1.union(s2))

print(s1,s2)

#add s1 in this value that not in s1 and take from s2
s1.update(s2)
print(s1,s2)
s2.update(s1)
print(s1,s2)

#print that value that both sets in comman

c1={"beg","pen","book","pencil","book","pencil"}
c2={"bottle","water","bottle","pen","pencil","pen"}

# print comman elements

c3=c1.intersection(c2)
print(c3)

#seco nd way to find comman elements 
c1.intersection_update(c2)
print(c1)

# print non-comman elements

c3=c2.symmetric_difference(c1)
print(c3)

#relation between two sets isdisjoint():
# if not comman element then true
# if comman element then false 

A1={1,2,3,4,5,6}
A2={7,8,9,0,12}    
print(A1.isdisjoint(A2))

#if one set include into second set then true otherwise false in issuperset()

B1={1,2,3,4,5,6}
B2={1,2,3,4}
print(B1.issuperset(B2))
print(B2.issuperset(B1))

# issubset()
   
print(B2.issubset(B1))

# add element in set s1.add()

S1={1,2,3,4,5,6}
S1.add(7)
print(S1)

# remove() and discard() REMOVE elements from the set

S2={1,2,3,4}
S2.remove(3)
print(S2)
S2.discard(2)
print(S2)

# Rendom valve remove(pop) from set

S3={2,3,4,5,6,7}
item=S3.pop()
print(S3)
print(item) # print removed item 


# delate whole set with error 

'''city={"amreli","surat","ahmedabad","Rajkot"}
del city
print(city)'''

# clear() clear all elements from set without error

city1={"amreli","ahmedabad","surat","Rajkot"}
city1.clear()
print(city1)

# if-else item in sets

info={"carla",19,False,5.9}
if "carla" in info:
    print("yes it's present")
else:
    print("no it's not present")
