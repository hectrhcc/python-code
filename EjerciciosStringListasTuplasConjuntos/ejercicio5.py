#Lo mismo que el ejercicio4 pero ordenando de mayor a menor.

lista = []
 
salir = False
 
while(not salir):
    numero = int(input("Dame un numero: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort(reverse=True) #ordena la lista
 
print(lista)