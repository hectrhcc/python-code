#Programa que obtenga el dígito
#verificador de un RUT Chileno.
print("Este programa define su dígito verificador")
rut=int(input("Ingrese su rut sin el dígito verificador:"))
pa=rut
c=2
sum=0
while rut>0:
    a1=rut%10
    rut=int(rut/10)
    sum+=(a1*c)
    c=c+1
    if c==8: 
      c=2
di=sum%11
digi=11-di
if digi==11:
	print("El dígito verificador es 0 =",pa,"-0")
if digi==10:
	print("El dígito verificador es K =",pa,"-K")
else:
    print("El dígito verificador es",digi,"=",pa,"-",digi)