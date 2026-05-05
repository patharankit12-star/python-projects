# lists

marks = [3,5,7,1,2,4,5,6,8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[1:]) #start with [1:len(marks[])]
print(marks[1:8:2]) # 1 to 1 



if 7 in marks:
    print("yes")
else:
    print("No")
#list index

colors = ["Red","Blue","Black","White","Orange"]
print(colors)
print(colors[-3])#negative index 5-3=2

if "Ha" in "Harry":
    print("yes")
else:
    print("NO")

#List Comprehension

lst=[i*i for i in range(10)]
print(lst)