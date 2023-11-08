from doctest import Example


my_object = ["kushagra", "mukund", "shanaz"]
iter_obj = iter(my_object)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj)) 
print(next(iter_obj))

#2nd sample
class Example:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        x = self.a
        self.a +=2
        return x
    itr = Example()
    my_iter = iter(itr)
    print(next(my_iter))
    