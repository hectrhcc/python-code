'''
Crea un programa que implementará sobre un diccionario una agenda formada por nombres de personas
(clave) y teléfonos (valor). Dicho programa dará las opciones de añadir una entrada (o modificarla si ya
existía), borrar una entrada (o avisar si no existía), listar la agenda, y salir.
'''

# Agenda

miAgenda = {}

while True:
		
    print()
    print('1. Insertar persona')
    print('2. Borrar persona')
    print('3. Listar personas')
    print('0. Salir')
    print('-------------------')
    opcion = input('Escoge opción: ')
    print()

    if opcion == '1':
        nombre = input('Nombre de la persona a introducir: ')
        telef = input('Teléfono de la persona a introducir: ')
        if nombre in miAgenda:
            print('Ya existía, pero cambio su teléfono')
        miAgenda[nombre] = telef

    elif opcion == '2':
        nombre = input('Nombre de la persona a borrar: ')
        if nombre in miAgenda:
            miAgenda.pop(nombre)
        else:
            print('Esta persona no existe')

    elif opcion == '3':
        for nombre in miAgenda:
            print(nombre, ':', miAgenda[nombre])
				
    elif opcion == '0':
        print('Adios')
        break

    else:
        print('Opción incorrecta')

