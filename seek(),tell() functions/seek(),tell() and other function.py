

#seek()

with open('file.txt','r') as f:
    print(type(f))
 # Move to the 8th byte in the file
    f.seek(8)

#Read the next 5oth byte that start with 8th byte
    print(f.tell()) # it's tell that which byte to we start it tell()
    data=f.read(50)
    print(data)

#truncate of file 

with open('file.txt','w') as f:
    f.write('Hello world!')
    f.truncate(5)  #truncate suggrsts that only first 5th character print 

with open('file.txt','r') as f:
    print(f.read())

