# Realice el análisis, diseño y codificación de un algoritmo que solucione el siguiente problema:
# Se tienen registrados en listas los datos de cada uno de los socios de un club de deportes: Nombre, Apellido, Edad,
# Sexo (hombre o mujer) y Tipo de deporte que practica (Tenis, Voley o Futbol). Construya un programa que presente
# un menú que permita:
#    1) Mostrar Apellido, Nombre, Edad y Sexo de los socios que practican Voley indicando cuántos son mujeres
#    y cuántos son hombres.
#    2) Mostrar la mayor edad de todas y el (o los) Apellido, Nombre, Sexo y Deporte de los socios que la tienen.
#    3) Mostrar el promedio de edad de los socios que practican Voley.
#    4) Salir

# Modalidad: Una lista por cada dato. La misma posición de las 5 listas corresponde a los datos de un socio.
nombres = ['Marcelo', 'Alicia', 'Luis', 'Claudia', 'Esteban', 'Pedro']
apellidos = ['Muñoz', 'Soto', 'Mamani', 'Rojas', 'Herrera', 'Vargas']
edades = [28, 23, 45, 32, 45, 45]
sexos = ['hombre', 'mujer', 'hombre', 'mujer', 'hombre', 'hombre']
deportes = ['Voley', 'Tenis', 'Futbol', 'Futbol', 'Voley', 'Voley']

# Mostrar el menú y solicitar una opción por primera vez.
print('Menú:')
print('1) Mostrar Apellido, Nombre, Edad y Sexo de los socios que practican Voley indicando cuántos son mujeres y cuántos son hombres.')
print('2) Mostrar la mayor edad de todas y el (o los) Apellido, Nombre, Sexo y Deporte de los socios que la tienen.')
print('3) Mostrar el promedio de edad de los socios que practican Voley.')
print('4) Salir')
opcion = int(input('Ingrese la opción a realizar: '))
while opcion < 1 or opcion > 4:
    print('La opción ingresada no es válida. Inténtelo de nuevo.')
    opcion = int(input('Ingrese la opción a realizar: '))
    
# Repetir el bucle while mientras que la opción ingresada por última vez sea distinta a 4. Es decir, el programa continúa ejecutándose.
while opcion != 4:
    if opcion == 1:
        cant_hombres = cant_mujeres = 0 # Asignar 0 estas variables "contadores" que sirven para saber cuánt@s mujeres/hombres practican Voley.
        print('\nResultado:')
        # Modalidad: Recorrer la lista deportes usando el índice de posición. 
        for i in range(len(deportes)):
            if deportes[i] == 'Voley':
                print(f'El socio {sexos[i]} {apellidos[i]}, {nombres[i]} de {edades[i]} años practica Voley.')
                if sexos[i] == 'hombre':
                    cant_hombres += 1
                else:
                    cant_mujeres += 1
        print(f'{cant_mujeres} es la cantidad de mujeres y {cant_hombres} es la cantidad de hombres.')
    elif opcion == 2:
        mayor_edad = 0 # Asignar 0 esta variable que sirve para encontrar la mayor edad entre los socios.
        # Modalidad: Recorrer la lista edades usando la variable sustituta. 
        for valor in edades:
            if valor >= mayor_edad:
                mayor_edad = valor
        print(f'\nResultado:\nLa mayor edad entre los socios es de {mayor_edad} años.')
        # Modalidad: Recorrer la lista edades usando el índice de posición. 
        for i in range(len(edades)):
            if edades[i] == mayor_edad:
                print(f'El socio {sexos[i]} {apellidos[i]}, {nombres[i]} que practica {deportes[i]} tiene {edades[i]} años.')
    else:
        suma_edades = 0 # Asignar 0 esta variable que sirve para sumar las edades de los socios que practican Voley.
        cant_socios = 0 # Asignar 0 esta variable que sirve para saber cuántos socios practican Voley.
        # Modalidad: Recorrer la lista deportes usando el índice de posición. 
        for i in range(len(deportes)):
            if deportes[i] == 'Voley':
                suma_edades += edades[i]
                cant_socios += 1
        promedio = suma_edades / cant_socios
        print(f'\nResultado:\nEl promedio de edad de los socios que practican Voley es de {round(promedio)} años.')
    # Mostrar el menú y solicitar una opción nuevamente.
    print('\nMenú:')
    print('1) Mostrar Apellido, Nombre, Edad y Sexo de los socios que practican Voley indicando cuántos son mujeres y cuántos son hombres.')
    print('2) Mostrar la mayor edad de todas y el (o los) Apellido, Nombre, Sexo y Deporte de los socios que la tienen.')
    print('3) Mostrar el promedio de edad de los socios que practican Voley.')
    print('4) Salir')
    opcion = int(input('Ingrese la opción a realizar: '))
    while opcion < 1 or opcion > 4:
        print('La opción ingresada no es válida. Inténtelo de nuevo.')
        opcion = int(input('Ingrese la opción a realizar: '))
        
print('\nResultado:\nEste menú ha sido cerrado.')
