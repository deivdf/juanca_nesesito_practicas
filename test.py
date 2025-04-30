def fib(a,b):
    if a == 0:
        return b
    else:
        return fib(b, a+b)