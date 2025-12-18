#Factorial Program
def fun(n):
    if n <=1:
        return 1
    return n * fun(n-1)
print(fun(5))

#Fibnacci Number
def fun(n):
    if n <=1:
        return n
    return fun(n-1)+fun(n-2)
print(fun(5))