#Lists method 

# l.append() add element in end of list
l=[1,2,3,4,5]
print(l)
l.append(6) #Add elements in end of list 
print(l)

#l.sort() Do sort list 

l=[4,2,3,7,10,34,123,1,2,3,90]
print(l)
l.sort() #accending order
print(l)
l.sort(reverse=True)
print(l)  #Decending order

#l.reverse() reverse list
l=[11,2,3,4,5]
l.reverse()
print(l)

#l.index find index this elements

l=[1,2,23,21,72,34,567,81]
print(l.index(2))

#l.count count element how mnay

l=[2,1,2,1,2,3,3,12,1,2,3]
print(l.count(1)) #how many time 1 in list

#l.copy() copy elements one to other
l=[1,2,3,4,5,6,7]
m=l
m[0]=0     #change in l list
print(l)


l=[1,2,3,4,5,6,7]
m=l.copy()
m[0]=0     #not change in l list
print(l)   #change ini m only
print(m)

#l.insert(1,56) Add 56 at 1st index improve list length 

l=[2,34,5,6,7,8,23,1]
l.insert(1,899) #Add 899 on first index and impore one length
print(l)

#l.extend() open that list and add previous list

l=[120,23412,78,90,87]
m=[900,123,1234]
l.extend(m)  #open m list and end of list l
print(l)
k= m + l
print(k)