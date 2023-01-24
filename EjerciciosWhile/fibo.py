i=0
def fib(n,i):
    a, b = 0,1
    while a < n:
        print("contador:",i)
        i+=1
        print(a, end=' ')
        a, b = b, a+b   
    #print(" a", a)
fib(8,0)