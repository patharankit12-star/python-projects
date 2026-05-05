# f-string 

name=input("Enter your name=")
country=input("Enter your country=")

letter="Hey my name is {} and I am from {}."
# This is old method
# l.format() enter in space strings 
print(letter.format(name,country))

# new method 
#f.string method
print(f"Hey my name is {name} and I am from {country}.")

#Example

price=49.0999999
print(f"For only {price:.2f} dollars!")


