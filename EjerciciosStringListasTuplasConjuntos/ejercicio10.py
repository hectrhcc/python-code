#Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). 
#Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.

agenda = {}
 
salir = False
 
while (not salir):
 
    #Pedimos los datos
    nombre=input("Introduce un nombre: ")
    telefono=int(input("Introduce un telefono: "))
 
    #Comprobamos si esta dentro del diccionario
    if(nombre not in agenda):
        #Añadimos el contacto
        agenda[nombre] = telefono
        print('Añadido el contacto')
    else:
        print('El nombre esta repetido')
         
    #Indicamos si queremos salir
    respuesta = input("¿Quieres salir? (S/N)")
 
    if(respuesta == "S"):
        salir = True
 
#Mostramos el diccionario
print(agenda)