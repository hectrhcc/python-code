#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar.
#Por último, muestra los números ordenados de menor a mayor.

lista = []
 
salir = False
 
while(not salir):
    numero = int(input("Dame un numero: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort() #ordena la lista
 
print(lista)