

'''f= open('hello.txt','r')
while True:
    line= f.readline()
    if not line:
        break
    print(line)'''

f=open('hello.txt','r')
i=0
while True:
    i = i + 1
    line = f.readline() #readline methods 
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"marks of student {i} in maths is:{m1}")
    print(f"marks of student {i} in english is:{m2}")
    print(f"marks of student {i} in SST is:{m3}")

#writelines method 

f=open('myfile2.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close
    