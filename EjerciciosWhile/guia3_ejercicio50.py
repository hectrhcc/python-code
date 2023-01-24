# En un club se registran por cada uno de sus socios: Número de socio (0 finaliza), Edad, Sexo (1:hombre, 2:mujer) y Tipo de
# deporte que practica (1:tenis, 2:rugby, 3:voley, 4:hockey, 5:futbol). Informar cuántos socios practican tenis y cuántos futbol,
# cuántos socios hombres practican hockey, cuantos socios mujer practican rugby, además promedio de edad de los socios de cada deporte.

# Suma de edades para cada tipo de deporte.
suma_tenis = suma_rugby = suma_voley = suma_hockey = suma_futbol = 0
# Contador de socios para cada tipo de deporte.
contador_tenis = contador_rugby = contador_voley = contador_hockey = contador_futbol = 0
# Contador de socios hombres para hockey y de socias mujeres para rugby.
contador_hombres_hockey = contador_mujeres_rugby = 0

# Solicitar el registro del primer socio.
num_socio = int(input('\nIngrese el número de socio (0 para finalizar): '))
while num_socio < 0:
    print('El valor ingresado no es aceptable por ser negativo. Inténtelo de nuevo.')
    num_socio = int(input('Ingrese el número de socio (0 para finalizar): '))

while num_socio != 0:
    edad = int(input('Ingrese la edad: '))
    while edad <= 0 or edad > 100:
        print('El valor ingresado está fuera del intervalo de edad. Inténtelo de nuevo.')
        edad = int(input('Ingrese la edad: '))
    sexo = int(input('Ingrese el sexo (1: Hombre, 2: Mujer): ' ))
    while sexo != 1 and sexo != 2:
        print('El valor ingresado no corresponde a ningún sexo. Inténtelo de nuevo.')
        sexo = int(input('Ingrese el sexo (1: Hombre, 2: Mujer): ' ))
    tipo_deporte = int(input('Ingrese el tipo de deporte que practica (1: Tenis, 2: Rugby, 3: Voley, 4: Hockey, 5: Futbol): '))
    while tipo_deporte != 1 and tipo_deporte != 2 and tipo_deporte != 3 and tipo_deporte != 4 and tipo_deporte != 5:
        print('El valor ingresado no corresponde a ningún tipo de deporte. Inténtelo de nuevo.')
        tipo_deporte = int(input('Ingrese el tipo de deporte que practica (1: Tenis, 2: Rugby, 3: Voley, 4: Hockey, 5: Futbol): '))
    # Informar cuántos socios practican cierto tipo de deporte. 
    if tipo_deporte == 1:
        contador_tenis = contador_tenis + 1
        suma_tenis = suma_tenis + edad
    elif tipo_deporte == 2:
        if sexo == 2:
            contador_mujeres_rugby = contador_mujeres_rugby + 1
        contador_rugby = contador_rugby + 1
        suma_rugby = suma_rugby + edad
    elif tipo_deporte == 3:
        contador_voley = contador_voley + 1
        suma_voley = suma_voley + edad
    elif tipo_deporte == 4:
        if sexo == 1:
            contador_hombres_hockey = contador_hombres_hockey + 1
        contador_hockey = contador_hockey + 1
        suma_hockey = suma_hockey + edad
    else:
        contador_futbol = contador_futbol + 1
        suma_futbol = suma_futbol + edad
    # Solicitar el registro de un nuevo socio.
    num_socio = int(input('\nIngrese el número de socio (0 para finalizar): '))
    while num_socio < 0:
        print('El valor ingresado no es aceptable por ser negativo. Inténtelo de nuevo.')
        num_socio = int(input('Ingrese el número de socio (0 para finalizar): '))

# Mostrar los datos de salida.
print('\nRESULTADOS:')
print(f'\n{contador_tenis} socio(s) practican tenis y {contador_futbol} socio(s) practican futbol.')
print(f'\n{contador_hombres_hockey} socio(s) hombre(s) practican hockey y {contador_mujeres_rugby} socia(s) mujer(es) practican rubgy.')
if contador_tenis != 0:
    promedio_tenis = suma_tenis/contador_tenis
    print(f'\n{round(promedio_tenis)} años es el promedio de edad de los socios que practican tenis.')
else:
    print('\nNo se encuentra registrado ningún socio que practique tenis.')
if contador_rugby != 0:
    promedio_rugby = suma_rugby/contador_rugby
    print(f'\n{round(promedio_rugby)} años es el promedio de edad de los socios que practican rugby.')
else:
    print('\nNo se encuentra registrado ningún socio que practique rugby.')
if contador_voley != 0:
    promedio_voley = suma_voley/contador_voley
    print(f'\n{round(promedio_voley)} años es el promedio de edad de los socios que practican voley.')
else:
    print('\nNo se encuentra registrado ningún socio que practique voley.')
if contador_hockey != 0:
    promedio_hockey = suma_hockey/contador_hockey
    print(f'\n{round(promedio_hockey)} años es el promedio de edad de los socios que practican hockey.')
else:
    print('\nNo se encuentra registrado ningún socio que practique hockey.')
if contador_futbol != 0:
    promedio_futbol = suma_futbol/contador_futbol
    print(f'\n{round(promedio_futbol)} años es el promedio de edad de los socios que practican futbol.')
else:
    print('\nNo se encuentra registrado ningún socio que practique futbol.')
    