def my_generator():
    for i in range(10):
        yield i 
gen = my_generator()
print(next(gen))       
print(next(gen)) 
print(next(gen)) 
print(next(gen))  
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 

#2nd code
def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

doubler = doubler_generator()
print (next(doubler))
print (next(doubler))
print (next(doubler))   
print (type(doubler))