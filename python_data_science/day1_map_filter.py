def cube(x):
    return x ** 3
list1 = [1,5,8,4,3,9,3,7]
new_list = list(map(cube, list1))#maps a function to every element in a sequence.
print(new_list)

#filter function

#  def filter_fun(a):
#      return a>4

# nenewl = list(filter(filter_fun, list1))
# print(nenewl)

def cube(x):
    return x ** 3

list1 = [1, 5, 8, 4, 3, 9, 3, 7]
new_list = []

for element in list1:
    new_list.append(cube(element))

print(new_list)
