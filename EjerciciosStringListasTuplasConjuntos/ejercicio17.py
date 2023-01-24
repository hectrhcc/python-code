'''
Crea un programa que dado una lista de 15 elementos con valores aleatorios, sea capaz de ordenar la lista
y dar el resultado por pantalla.
'''
import random

NUM_ELEM = 15


# Rellenamos la lista con números aleatorios.

lista = [random.randint(1, 100) for e in range(NUM_ELEM)]

print('Lista sin ordenar: ', lista)


lista.sort()

print('Lista ordenado: ', lista)
