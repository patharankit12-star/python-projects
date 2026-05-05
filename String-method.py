# String are immutable

#String in uppper and lower case
a="SarKar"
print(len(a))
print(a.upper())
print(a.lower())

#string in rstrip() remove characters in tralling

b="welcome!!!!!!!!!"
print(b)
print(b.rstrip("!"))

#string in replace()
c="goodmorning!!!!!!!!goodmorning"
print(c.replace("goodmorning","goodnight"))

#string in split() convert into list after space

d="Ram nam shyam"
print(d.split(" "))

#String in capitalize() convert capital

E="introduction to me!"
print(E.capitalize())

#string in center() located into the center

str1="Welcome to python!!!"
print(len(str1))
print(len(str1.center(40)))
print(str1.center(40))

#string in count() count the name 
G="hp Dell hp Dell asus hp Dell Dell asus"
print(G.count("hp"))
print(G.count("Dell"))
print(G.count("asus"))

#string in startwith() if start with thar characters then true otherwith false

ASN="@@@ welcome!!"
print(ASN.startswith("@@@"))

#string in endswith() if end with that characters  True or False 

str2="Welcome coder###"
print(str2.endswith("###"))
print(str2.endswith("@@@"))

str3="welcome to the console!!!"
print(str3.endswith("to",4,10))

#String in find() return  first index

str4="He is good man"
print(str4.find("is"))#'i' index 
print(str4.find("ishhh"))#return -1

#string in index() find index

H="Happy"
print(H.index("a"))

#string in isalnum() A-Z a-z 0-9 then return True otherwise false

I="Welcometopark!!"
print(I.isalnum())

#string in isalpha() True return then A-Z and a-z olny not num

J="welcome"
print(J.isalpha())

#string in islower() , if lower case then true otherwise false

K="welCome"
print(K.islower())

#string in if all vlue is printable then true otherwise false

L="How are you!"
print(L.isprintable())
M="How are you\n"
print(M.isprintable())

#string in isspace() if  only space in string then true

N="    "
print(N.isspace())

#string in if title not captilize then istitle() return flase otherwise true

O="welcome to helth organization"#lower conditions
print(O.istitle())

P="Welcome To My House!!"
print(P.istitle())#upper conditions

#string in convert into title style 

Q="His is honest man."
print(Q.title())

#string in swapcase upper to lower and lower to upper

R="Python is a Interpreted Language"
print(R.swapcase())