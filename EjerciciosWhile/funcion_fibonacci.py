def fib(n):
    a=0
    b=1
    for k in range(n):
        c = a + b 
        a = b
        b = c
    return a

for x in range(20):
    print(fib(x))