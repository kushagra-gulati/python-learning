def calculate(a,b):
    if (a>b):
        print("a is greater than b")
    else:
        print("b is greater than or equal to a")

a = 45
b = 47
calculate(a,b)
        
# name = "kushagra"
def func():
   global name
   name = "Stark"

func()
print(name)  # Accessing 'name' outside the function
#3rd probelm statement
name = "Ned"





def func(name):
    name = "Stark"
    print(name)


func(name)
print(name)
  # The value of 'name' remains unchanged.
  

  #4th sample problem statement
  string1 = "there was a boy name kushagra, he is mad all the time"
  print(len(string1))

 