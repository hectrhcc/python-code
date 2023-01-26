#este es un comentario en python
print("hola python\n")
#variables
print("Variables\n")

numero = 5
texto = "esto si que es cuatico"
booleano = True
edad = 29
#no existen las constantes en python
MI_CONSTANTE = 4

#imprimiendo  variable tipo numero
print("numero:",numero)
#imprimiendo variable tipo string
print("texto:",texto)
#imprimiendo  variable tipo booleano
print("booleano:",booleano)
#probando variable edad
print("mi edad es ", edad)
edad = 25
print("mi edad ahora es ", edad)
#probando constante
print("constante:", MI_CONSTANTE)
MICONSTANTE= 1234
print("constante otra otra vez:", MI_CONSTANTE)
#imprimiendo una variable
resultado = 2+3
print("el resultado es: ", resultado)

#Ingreso de un numero entero
numero_entero = int(input("Ingrese un numero entero:"))
print("El numero entero ingresado es:",numero_entero,"\n")


#condicionales
print("Condicional if, elif y else\n")

respuesta = str(input("¿Quiere una pizza vegetariana? responda solo con si o no:"))
if (respuesta=="si"):
	pizza ="vegetariana"
	print("ingredientes disponibles: \n1-Pimiento\n2-Tofu")
	ingrediente=int(input("Ingrese el numero del ingrediente:"))
	if (ingrediente==1):
		ing= "pimiento"
	else:	
		ing = "tofu"
else:
	pizza = "no vegetariana"
	print("ingredientes disponibles: \n1-Peperoni\n2-Jamon\n3-Salmon")
	ingrediente=int(input("Ingrese el numero del ingrediente:"))
	if (ingrediente==1):
	 	ing= "peperoni"
	elif (ingrediente==2):	
		ing = "jamon"
	else:
		ing = "salmon"
print("La pizza seleccionada es",pizza ," y el ingrediente es:\n",ing ,",tomate y mozzarrella\n")


#probando el operador AND y OR ( && ||)
print("Operador and y or  o && y ||")
num =9
nombre="Fernando"
if(num == 9 or nombre=="Francisco"):
	print('Si, si es el mismo numero o nombre\n')
elif(num== 9 and nombre=="Fernando"):
	print('Si, si es el mismo numero y nombre\n')
else:
	print('No, no es el mismo numero ni nombre\n')

#probando el bucle while
print("Bucle While\n")
contador =0
while(contador <10):
	print("esto se esta repitiendo:",contador,"\n")
	contador+=1

#probando el bucle For
print("Bucle For\n")

for x in range(1,10):
	print(x)

for i in range(5):
	print(i)
else:
	print("esto es un else\n")

numeros= [10,20,30,40,50,60,70,80,90,100,110]

for numero in numeros:
	print(numero)


#probando funciones
print("\nFunciones\n")

def primera():
	print("esto es una funcion\n")

# llamada
primera()

#funcion 2

def segunda(nombre):
	print("esta es otra funcion con un argumento: " +nombre)

# llamada
segunda("argumento")

#funcion 3


def tercera(num1,num2):
	resultado = num1*num2
	print("el resultado de la multiplicacion es:", resultado)
	return resultado
valor = tercera(6,7)
print(valor)


#funcion 4

def multiplicar(num1,num2):
	result = num1 * num2
	return result
print(multiplicar(8,9))

#probando vectores
print("\nVectores\n")
vector = [1]*5


for i in range(0,5):
	print(vector[i])

#probando listas
print("\nListas\n")
lista1 =[1,2,3]
lista2 =['a','b','c']
lista3 =lista1+lista2
print(lista3)

lista2.append('d')
print(lista2)

lista3.remove("c")
print(lista3)
# lista de lista

lista4 = [lista1,lista2,lista3]

print(lista4)


#probando tuplas
print("\nTuplas\n")
tupla1 =("manzana", "platano", "cereza", "limon", "uva")
print(tupla1[2:5]) # Elementos desde el índice 2 hasta el índice 5-1
print(tupla1[0:2]) # Elementos desde el índice 0 hasta el índice 2-1

tupla2 = (tupla1, "piña","fresa")

print(tupla2)


#probando diccionario
print("\nDiccionario\n")
diccionario = {
"clave":"valor", 
"nombre":"Boris", 
"edad":28,
"amigos":["Marcelo","Victor","Nicolas","Jeremias"]	
}
diccionario2 = {
"llave":"valor", 
"nombre":"Agro", 
"edad":22
}

print(diccionario)
print(diccionario2)


#clases y objetos
print("\nClases y Objetos\n")
class Objeto(): 
    color = "blanco" 
    tamanio = "grande" 
    aspecto = "hermoso" 
  

    def saludar(): 
        print("hola, soy un objeto que te saluda")

o = Objeto() 
print(o.color) 
print(o.tamanio) 
print(o.aspecto)
o.color = "rosa" 
print(o.color)
Objeto.saludar()