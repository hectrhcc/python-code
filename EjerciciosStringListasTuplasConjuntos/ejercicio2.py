#!/usr/bin/python3
#Crea una tupla con los meses del año, pide números al usuario, si el número esta entre 1 y la longitud
#máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa
#termina cuando el usuario introduce un cero.
 
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
 
salir = False
while(not salir):
     
    numero = int(input("Dame un numero: "))
 
    if(numero==0):
        salir= True
    else:
        if(numero>=1 and numero<=len(meses)):
            print(meses[numero-1])
        else:
            print("Inserta un numero entre 1 y ",len(meses))