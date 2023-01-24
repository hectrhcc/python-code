'''
Crea un programa que dados dos listas las convierta en un diccionario, en el que los elementos de la
primera lista eran las claves y los elementos de la segunda lista eran los valores asociados a dichas claves.

'''

# Ejemplo de transformación de listas en diccionarios

claves  = ['rojo', 'verde', 'azul']
valores = ['#FF0000','#008000', '#0000FF']
colores = {} 
for i in range(len(claves)):
    colores[claves[i]] = valores[i] 
print(colores)



# Se podía hacer también utilizando las funciones zip() y dict() de Python
#  - https://docs.python.org/3/library/functions.html#zip
#  - https://docs.python.org/3/library/stdtypes.html#dict

claves = ['rojo', 'verde', 'azul']
valores = ['#FF0000','#008000', '#0000FF']
colores = dict(zip(claves, valores))
print(colores)


