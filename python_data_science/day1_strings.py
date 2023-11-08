print('A string is a sequence (a positionally ordered collection) of other objects or elements.')
print("A string is a sequence (a positionally ordered collection) of other objects or elements.")

#FORMAT METHOD
name = "KUSHAGRA GULATI"
name2 = "KUNAL JAIN"
age = 24
city = "MEERUT"
print("Hello guys My Name is {} and My Age is {}".format(name,age))

#format 2nd type
print("Hello guys My Name is {one} and My Age is {two} and city is {three}".format(one=name,two=age,three=city))


#accessing strings using format method in print
print("Hello guys My Name is {} and My Age is {}".format(name[1],age))
#or
print("Hello guys My Name is {} and My Age is {}".format(name[0:6],age))


#concatenation
full_name = name + name2
print(type(full_name))
print("Our full name  is :- ",full_name)


#lower,upper method in string
print("Hello guys My Name is {} and My Age is {} and other name is {}".format(name.lower(),age,name2.upper()))

#split
print("Hello guys My Name is {} and My Age is {}".format(name,age))

print(type(name.split()))