num1 = 5
num2 = 10787654
num3 = 10787654
list1 = [6,7,8]
list2 = [6,7,8]


print(num2 is not num3) 
print(id(num2), id(num3))
print(list1 is list2)  

a=10
a=11

print("aaaaab" < "aaaaac")
print(list1 is list2) 

year = 2019
print(year)

year = 2020
print(year)

year = year + 1  
print(year)

year = year +3
print(year)

first = 20
second = first
first = 35 

print(first, second)  # unchanging the first value not second onwards
print(10 * False)
print(10 + True)

num1 = 10  
num2 = 20  

print(num1 & num2)   
print(num1 | num2)   
print(num1 ^ num2)   
print(~num1)         
print(num1 << 3)     
print(num2 >> 3)   

print('a' < 'b') 

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"

print(house == new_house)

print(new_house <= house)

print(new_house >= house)

print ("G"<="S")
print(new_house <= house)

print("kush " *4)

myname = "my name is kushagra gulati, i live in meerut"
print("live" in  myname)

firstlist = [1,2,394, "hi my name is kushagra"]
print(firstlist[0:2])

x = 20
y = 5
result = (x + True) / (4 - y * False)
print(result)