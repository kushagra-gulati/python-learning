list1 = ["kushagra", "prerna", "kunal", "khali", "mukund" ,"mayank"]
a = " and ".join(list1)
print(a, "nd other players in the tournament")

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


result = calculator(multiply, 10, 20)
print(result)
res=int(calculator(divide, 100, 20))
print(res)

String = "Hey, My name is kushagra gulati , i belong to a city called Meerut "
# default sep, which is a white space.
print(String.split())


name = "kushagra"
last_name = "gulati"
age = 23
print('my name is {} {} and my age is {}'.format(name,last_name,age))