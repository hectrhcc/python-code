'''
Crea un programa que dados dos listas ordenadas realice la fusión de ambas para obtener una tercera lista
también ordenada. Cada lista contiene cinco elementos.
'''
print('Fusión de dos listas ordenadas')
print('--------------------------------\n')

# Pedimos la primera lista

cadena = input('Introduce los elementos de la primera lista separados por un espacio: ')
lista1 = [int(i) for i in cadena.split(' ')]

# Pedimos la segunda lista

cadena = input('Introduce los elementos de la segunda lista separados por un espacio: ')
lista2 = [int(i) for i in cadena.split(' ')]


# vectorR = sorted(vector1 + vector2) seria más corto, pero ineficiente

Lista3 = lista1 + lista2


# Imprimimos la lista fusionado

print('Lista fusionada: ', Lista3.sort())
