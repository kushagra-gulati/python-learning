class MyClass:
    pass


obj = MyClass()  # creating a MyClass Object
print(obj)

obj1 = MyClass()

# class 2n sample
class organisation: #creating class
    id = 125458751
    name = "kushagra gulati"
    age = 234
    salary = 54000

kushagra = organisation() #object accessing
print(kushagra.id)

# 3rs sample
class nocode:
    id: None
    name: None
    salary: None
    
kushagra = nocode()
kushagra.name= "kushagra gulati" # type: ignore
kushagra.id = 53725 # type: ignore
kushagra.salary = 25845 # type: ignore
print(kushagra.name)

