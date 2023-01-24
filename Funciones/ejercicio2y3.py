#Análisis:

#Datos de entrada: número entero 
#Datos de salida: cantidad de digitos que tiene
#el número y la suma de sus digitos

#Diseño:
#Solicitamos un número entero
#llamada a la función 
#quito los digitos al numero por division entera o truncar y los cuento
#retornar cantidad de digitos
#llamada a la funcion
#obtengo los digitos con el módulo 10 y los sumo
#retornar la suma de sus digitos

def funcion_cantdigito(x):
    cont=0
    while x>0:
       cont+=1
       x//=10
    return cont

def funcion_sumadigito(y):
    suma=0
    while y>0:
        dig = y%10
        #dig =int(y/10)
        suma+=dig
        y//=10
    return suma

num=int(input("Ingrese un número entero:"))
print("la cantidad de digito es:",funcion_cantdigito(num))
print("la suma de sus digitos es:",funcion_sumadigito(num))
