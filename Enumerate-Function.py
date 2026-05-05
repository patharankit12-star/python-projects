
marks=[12,23,34,56,12,7]

index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("now we on index 3")
        
    index= index + 1

# Enumerate function can short form of for loop code
# Remove index=0 , index = index + 1
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("Welcome to index 3")
    #index=index + 1