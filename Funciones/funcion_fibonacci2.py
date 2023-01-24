#Función Fibonacci
def fibonacci(limit):
    valores = []
    a,b = 0, 1 
    while len(valores) < limit:
    	valores.append(b)
    	a,b = b, a + b
    return valores 

n=int(input("Ingrese el número de término de la sucesión de fibonacci:"))

for x in range(n+1):
    vals = fibonacci(x)
    print(x, list(vals))