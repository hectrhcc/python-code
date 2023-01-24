i=0
h=[]
n = int(input("Ingrese la cantidad de números:"))
while i!=n:
	x=int(input("Ingrese el n°:"))
	mayor=x
	menor=x
	h.append(x)
	#print("h es",h)
	i+=1
j=n-1
while j!=-1:
	if mayor<h[j]:
            mayor=h[j]
	elif menor>h[j]:
            menor=h[j]
	j-=1
print("El número mayor es:", mayor," y el menor es:",menor)