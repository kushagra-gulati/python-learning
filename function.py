def my_first_function():
    print("My name ")
    print("Is")
    print("Kushagra Gulati")

print(my_first_function())
# my_first_function()

def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)


def minimum(first, second):
    if first < second:
        return first
    return second


num1 = 10
num2 = 20

result = minimum(num1, num2)  # Storing the value returned by the function
print(result)