'''
Crea un programa para rellenar una lista de 15 número enteros:
a. Con valores aleatorios entre 1 y 10, y a continuación diga cuántos pares e impares hay.
b. Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones que son
múltiplos de 3.
c. Con los primeros valores de la serie de Fibonacci.
d. Con valores introducidos por el usuario, y a continuación que los imprima al revés.
e. Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta que esté
entre 1 o 10.
f. Con valores introducidos por el usuario, que deben formar una secuencia creciente.
g. Con valores introducidos por el usuario, que no deben estar repetidos.

Obs: La instrucción de Python que te permite generar un número aleatorio entre a y b, ambos
incluidos, es random.randint(a, b)
'''

import random

MAX = 15



# a) Con valores aleatorios entre 1 y 10,
#    y a continuación diga cuantos pares e impares hay.

v = []

for i in range(MAX):
    v.append( random.randint(1, 10) )

print(v)

pares = 0
impares = 0

for e in v:
    if (e % 2) == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print('Hay', pares, 'pares y ', impares, 'impares')



# b) Con valores aleatorios entre 1 y 10,
#    y a continuación sume los que estén en posiciones que son múltiplos de 3. 

v = []

for i in range(MAX):
    v.append( random.randint(1, 10) )

print(v)

suma = 0

for i in range(0, len(v), 3):
    suma = suma + v[i]

print('La suma de las posiciones múltiplo de 3 es', suma)



# c) Con los primeros valores de la serie de Fibonacci.

v = [0, 1]

for i in range(2, MAX):
    v.append( v[i-1] + v[i-2] )

print(v)



# d) Con valores introducidos por el usuario, 
#    y a continuación que los imprima al revés.

v = []

for i in range(MAX):
    v.append( input(f'¿Qué valor para la casilla {i}? ') )

for i in range(len(v)-1, -1, -1):
    print(v[i], '  ', end='')
print()



# e) Con valores introducidos uno a uno por el usuario,
#    que debe pedir hasta que estén entre 1 o 10.

v = []

for i in range(MAX):
    x = float( input(f'¿Qué valor para la casilla {i}? ') )
    while x < 1 or x > 10:
        print('Valor incorrecto. Debe estar entre 1 y 10.')
        x = float( input(f'¿Qué valor para la casilla {i}? ') )
    v.append( x )

print(v)



# f) Con valores introducidos uno a uno por el usuario,
#    que deben formar una secuencia creciente.

v = []

for i in range(MAX):
    x = float( input(f'¿Qué valor para la casilla {i}? ') )
    while i > 0 and v[i-1] > x:
        print('Valor incorrecto. Debe ser creciente.')
        x = float( input(f'¿Qué valor para la casilla {i}? ') )
    v.append( x )

print(v)



# g) Con valores introducidos uno a uno por el usuario,
#    que no deben estar repetidos.
#    Sin utilizar vector.index(elemento) ni vector.count(elemento)
#    ni el operador in.

v = []

for i in range(MAX):
    x = input(f'¿Qué valor para la casilla {i}? ')

    while True:
        encontrado = False
        for j in range(i):
            if x == v[j]:
                encontrado = True
        if encontrado:
            print('Valor incorrecto. No puede estar repetido.')
            x = input(f'¿Qué valor para la casilla {i}? ')
        else:
            v.append( x )
            break

print(v)
