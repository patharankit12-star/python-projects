# Walrus Operator := --->using convert alternative 

a=True 
print(a := False)

#Example

numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

#Example

foods = list()

while (food := input("what food you like?: ")) != "quit":
    foods.append(food)