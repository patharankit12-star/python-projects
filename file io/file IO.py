
# read file 
f = open('hello.txt', 'r')
text = f.read()
print(text)
f.close()

#  open and write file 
f=open('myfile2.txt','w') # Here 'w' replace with 'a' also
f.write("hello brother")
f.close()

# replace f.close() automatic replace by with statement 

with open('hello.txt','a') as f:
    f.write("hey i am inside hello file:")
