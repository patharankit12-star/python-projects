# can not change in tuple directly

countries=("spain","italy","India","USA")
temp=list(countries)
temp.append("Russia") #ADD ITEM
temp.pop(3)          #remoove item
temp[2]="finland"     #change item
countries=tuple(temp)
print(countries)

#create tuple from tuples

num1=(1,2,3,4)
num2=(5,6,7)
num3=num1 + num2 #sum of two tuples
print(num3)

#count() in tuple

tuple1=(0,1,3,2,3,1,4,0)
res=tuple1.count(3)
print("count of 3 in tuple is :",res)

#index() in tuple index of tuples element

tup=(1,2,3,4,3,3,7)
res=tup.index(3)
print("index of 3 is:",res)
res1=tup.index(3,2,6)
print("count of 3 between 2-6 index:",res1)