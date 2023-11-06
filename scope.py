def my_func(a, b):
    print(x) #local variable defined wrong
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)


    
    global c
    # swap a and b
    b, a = a, b
    d = 'Mike'
    print(a, b, c, d)

a, b, c, d = 1, 2, 'c is global', 4
my_func(1, 2)
print(a, b, c, d)

