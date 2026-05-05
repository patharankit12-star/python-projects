# Generators use for make function that make momary  that required as per it need
# not store value like list that generator have components for make again value
# use in large number of data 
def my_Generator():
    for i in range (50):
        yield i

gen =my_Generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# need short time 
for j in gen:
    print(j)
