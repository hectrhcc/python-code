i=0
k=0 #anterior al anterior
j=1 #anterior 
n=int(input("Ingrese un número para la serie de fibonacci:"))
while i<n:
    print("Elemento",i,"=",k)
    k,j = j, j+k # j (f(-1) + f(-2)
    print(" ")
    print("k",k)
    print("j",j)
    print(" ")
    i+=1
