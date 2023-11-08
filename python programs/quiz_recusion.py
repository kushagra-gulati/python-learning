#starting of code
def rep_cat(x,y):
    return str(x)*10 + str(y)*5
print(rep_cat(4,8))

#factorial
def fact(n):
    if (n ==0  or n ==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

def factorial(n):
    if (n ==0  or n ==1):
        return 1
    if n < 0:
        return -1
        return n * factorial(n-1)
    
print(factorial(3))