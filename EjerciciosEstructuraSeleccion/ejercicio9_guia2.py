#Este algoritmo solo funciona con todos los numeros iguales y todos los numeros distintos
#obtiene el menor y el mayor y los intermedios,pero cuando se repiten numeros y no existen intermedios
#la variable intermedio no tomara ningun valor, tomara solo el valor inicial dando otro resultado al esperado
print("<<Ingrese numeros distintos>>")
num1 = int(input("Ingrese numero 1:"))
num2 = int(input("Ingrese numero 2:"))
num3 = int(input("Ingrese numero 3:"))
num4 = int(input("Ingrese numero 4:"))

mayor= num1
menor= num1
intermedio1 =num1
intermedio2 =num1

if num2>mayor:
    mayor = num2
else:
    menor = num2
if num3> mayor:
     mayor = num3
elif num3<menor:
     menor = num3
if num4> mayor:
     mayor = num4
elif num4 < menor:
     menor = num4

if (num1>menor) and (num1<mayor):
    intermedio1 = num1
elif (num2>menor) and (num2<mayor):
    intermedio1 = num2
elif (num3>menor) and (num3<mayor):
    intermedio1 = num3
elif (num4>menor) and (num4<mayor):
    intermedio1 = num4

if (num1>menor) and (num1<mayor) and (num1!=intermedio1):
        intermedio2 = num1
elif (num2>menor) and (num2<mayor) and (num2!=intermedio1):
        intermedio2 = num2
elif (num3>menor) and (num3<mayor) and (num3!=intermedio1):
        intermedio2 = num3
elif (num4>menor) and (num4<mayor) and (num4!=intermedio1):
        intermedio2 = num4

print("intermedio1", intermedio1)
print("intermedio2", intermedio2)
if intermedio2 <= intermedio1:
    print("Orden Descendente: ", mayor, intermedio1, intermedio2, menor)
#elif intermedio1 > intermedio2:
#print("Orden ascendente: ", menor, intermedio2, intermedio1, mayor)
else:
    print("Orden Descendente: ", mayor, intermedio2, intermedio1, menor)

