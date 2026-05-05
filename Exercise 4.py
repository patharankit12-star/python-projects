# Exercise 4

name=input("Enter the word:")

l=len(name)
print(l)
if(l<=2):
   name2="".join(reversed(name))
   print(name2)
elif(2<l<6):
   name3="".join(reversed(name))
   print(f"ido{name3}odi")
elif(6<=l):
   print(f"@@@{name[2]}{name[3]}{name[1]}{name[4]}{name[5]}###")


# solution

# 1. remove first charcter at last and print that
st=input("enter your massage:")
coding=input("1 for coding or 0 for Decoding")
coding=True if coding=="1" else False
 #True is coding and False is De-coding
if(coding):
   if(len(st)>=3):
      st=st[1:] + st[0]
      st3="".join(reversed(st))
      
      st2= "wdwdc" + st3 + "nfnerivf"
      print(st2)

else:
   if(len(st)>=3):
      st1=st[5:-8]
      st2=st1[1:] + st1[0]
      st3=" ".join(reversed(st2))
      print(st3)
