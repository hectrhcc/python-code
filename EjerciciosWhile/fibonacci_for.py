def fib(n):
    a=0# inicio
    b=1# inicio
    for k in range(n):
        c = a + b # a el valor funcion anterior al anterior + el valor funcion anterior
        a = b
        b = c
    return a

for x in range(20):
    print(fib(x))