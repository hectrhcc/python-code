i=0
k=0 #anterior
j=1 #anterior 0..
n=int(input("Ingrese un número para la serie de fibonacci:"))
while i<n:
    print("Elemento",i,"=",k)
    j=j+k
    k = j
    print(" ")
    print("k",k)
    print("j",j)
    print(" ")
    i+=1

