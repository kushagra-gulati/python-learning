def factorial(n):
    if(n==0 and n==1):
        return 1
    else:
        return n * factorial(n-1)
    
    print(factorial(3))
    print(factorial(4))


def fibonnaci(n):
    if(n <0):
        return 1
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)